from States.base_state import State 
from Game.map import Map 
from Entities.Towers.Bird_Flamethrower_tower import BirdFlamethrower
from Entities.Towers.Bomb_tower import Bomb
from Entities.Towers.Laser_tower import Laser
from Entities.Towers.Saw_tower import Saw
from Entities.Towers.Turret_Tower import Turret

from Game.game_data import ENEMY_CLASS_MAP

from UI.Menus.in_game_menu import GameButtons
from UI.Menus.tower_selection_menu import TowerSelectionMenu
from Game.mouse import Mouse
from Game.wave_manager import WaveManager

import pygame
class Game_State(State):
    """Main game engine - Manages the in-game logic, events, and rendering"""

    def __init__(self, game):
        """
        Initializes the Game_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        """
        super().__init__(game)  # Call the parent State class constructor
        
        # Initialize game map
        self.map = Map("Demonstration_Map")  # Stub/demonstration map
        
        # Dictionary to store towers (key: grid position, value: tower object)
        self.towers = {}

        # List to store active enemies
        self.enemies = []

        self.gamebuttons = GameButtons(self.game)
        self.tower_selection_menu = TowerSelectionMenu(self.game)

        self.mouse = Mouse()

        self.wave_manager = WaveManager(self.game)

        self.difficulty = "Normal"
        self.health = 100 # Placeholder health value
        self.money = 5000 # Placeholder money value

    def enter(self, *args):
        if args:
            level_name = args[0]
            self.level = level_name
            self.map = Map(level_name)
        print(f"Entering level {self.level}")

    def change_difficulty(self, difficulty):
        self.difficulty = difficulty

    def update(self, events):
        """
        Updates the game based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        self.mouse.update_mouse_pos()
        self.update_enemies()  # Update enemy positions and check for removals
        self.update_towers()   # Update tower behavior (attacking, targeting, etc.)
        self.check_bullet_collisions()  # Check and handle bullet collisions with enemies
        self.wave_manager.update()
        self.handle_events(events)  # Process player input and other events

    def update_enemies(self):
        """Update each enemy's movement and remove dead or finished enemies."""
        for enemy in self.enemies:
            enemy.update()
            if enemy.is_dead or enemy.reached_end:
                self.enemies.remove(enemy) # Remove enemy once reached end
                if enemy.is_dead:
                    self.money += enemy.reward # Reward money for enemy kill
                if enemy.reached_end:
                    self.health -= enemy.damage # Subtract health for failure to prevent enemy reaching end

    def update_towers(self):
        """Update all towers, making them attack enemies if applicable."""
        for _, tower in self.towers.items():
            tower.update(self.enemies)

    def check_bullet_collisions(self):
        """Check for bullet collisions with enemies and apply damage if hit."""
        for _, tower in self.towers.items():
            for bullet in tower.bullets:
                for enemy in self.enemies:
                    if pygame.Rect.colliderect(bullet.hitbox, enemy.hitbox):  # Check collision
                        enemy.take_damage(tower.bullet_damage)  # Apply damage
                        bullet.active = False  # Mark bullet as inactive after hitting an enemy

    def draw(self, screen):
        """
        Handles rendering the game to the screen.

        Args:
            screen: pygame display surface
        """
        self.map.draw(screen, self.mouse.map_grid_x, self.mouse.map_grid_y)  # Draw the game map
        self.draw_towers(screen)  # Draw all towers
        self.draw_enemies(screen)  # Draw all enemies
        self.gamebuttons.draw(screen)
        self.tower_selection_menu.draw(screen)


    def draw_towers(self, screen):
        """Draw all towers on the screen."""
        for _, tower in self.towers.items():
            tower.draw(screen)

    def draw_enemies(self, screen):
        """Draw all enemies on the screen."""
        for enemy in self.enemies:
            enemy.draw(screen)

    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.gamebuttons.buttons:
                    if button.is_hovered():
                        button.click()

                for button in self.tower_selection_menu.buttons:
                    if button.is_hovered():
                        button.click()

                if self.mouse.current_action == "Placing Tower":
                    self.place_tower()

                if self.mouse.current_action == "Removing Tower":
                    self.remove_tower()

    def place_tower(self):
        """
        Places a tower on the map grid and adds the selected tower to the game_state tower dict
        """
        if self.money >= self.mouse.current_selection(0,0).cost:
            if self.map.place_tower(self.mouse.map_grid_x, self.mouse.map_grid_y): # If able to place tower
                self.create_tower(self.mouse.current_selection, (self.mouse.map_grid_x, self.mouse.map_grid_y)) # Create new tower object
                self.money -= self.mouse.current_selection(0,0).cost # Removes the cost of the tower from money
                print(f"successfully placed tower, tower list is{self.towers}") # print dictionary of towers for debugging purposes
                self.mouse.change_current_action(None, None) # Reset mouse action and selection


    def remove_tower(self): # If able to remove tower
        """
        Removes a tower on the map grid and removes the selected tower from the game_state tower dict
        """
        if self.map.remove_tower(self.mouse.map_grid_x, self.mouse.map_grid_y):
            del self.towers[(self.mouse.map_grid_x, self.mouse.map_grid_y)] # Delete selected tower object (at selected map coordinate)
            print(f"successfully deleted tower, tower list is{self.towers}") # print dictionary of towers for debugging purposes
            self.mouse.change_current_action(None, None) # Reset mouse action and selection

    def create_enemy(self, enemy_name):
        print(f"created enemy {enemy_name}")
        enemy_class = ENEMY_CLASS_MAP.get(enemy_name)
        if enemy_class:
            self.enemies.append(enemy_class(self.map.enemy_start_pos, self.map.enemy_path))
        
    def create_tower(self, tower, position):
        self.towers[(self.mouse.map_grid_x, self.mouse.map_grid_y)] = tower(*position)