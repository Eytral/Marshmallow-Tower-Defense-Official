from States.base_state import State 
from Game.map import Map 
from Entities.Towers.Bird_Flamethrower_tower import BirdFlamethrower
from Entities.Towers.Bomb_tower import Bomb
from Entities.Towers.Laser_tower import Laser
from Entities.Towers.Saw_tower import Saw
from Entities.Towers.Turret_Tower import Turret
from Constants import config

from Game.game_data import ENEMY_CLASS_MAP, GAME_DATA

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

        self.mouse = Mouse()

        self.gamebuttons = GameButtons(self.game)
        self.tower_selection_menu = TowerSelectionMenu(self.game)

        self.wave_manager = WaveManager(self.game)

        self.difficulty = "Normal"
        self.starting_money = GAME_DATA[self.difficulty]["Game_Stats"]["Starting Money"]
        self.money = self.starting_money
        self.starting_health = GAME_DATA[self.difficulty]["Game_Stats"]["Starting Health"]
        self.health = self.starting_health

        self.total_error_message_display_time = 100
        self.error_message_display_time = 0
        self.error_font = pygame.font.Font(None, 50)
        self.error_message = None

    def enter(self, *args):
        """
        Enters the Game_state, setting the level that will be played, and calling the load level function to load such level

        Args:
            level_number: integer number representing the level that is being loaded
        """
        if args:
            level_name = args[0]
            self.level = level_name
            self.map = Map(level_name)
            print(f"Entering level {self.level}")
        self.wave_manager.reset_waves()
        self.health = self.starting_health
        self.money = self.starting_money

    def exit(self, **kwargs):
        exiting_game = kwargs.get("exiting_game", True)
        if exiting_game:
            self.map.reset_map()
            self.enemies = []
            self.towers = {}
            self.mouse.change_current_action(None, None)
            print("Game successfully exited")

    def change_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.wave_manager.difficulty = difficulty
        self.starting_health = GAME_DATA[self.difficulty]["Game_Stats"]["Starting Health"]
        self.starting_money = GAME_DATA[self.difficulty]["Game_Stats"]["Starting Money"]
        print(f"Successfully changed difficuty to {difficulty}")

    def update(self, events):
        """
        Updates the game based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        for button in self.tower_selection_menu.buttons:
            if button.is_hovered():
                self.mouse.currently_hovering = button.text
            
        self.mouse.update_mouse_pos()
        self.update_enemies()  # Update enemy positions and check for removals
        self.update_towers()   # Update tower behavior (attacking, targeting, etc.)
        self.check_bullet_collisions()  # Check and handle bullet collisions with enemies
        self.wave_manager.update()
        self.check_game_over()
        self.check_win()
        self.handle_events(events)  # Process player input and other events

    def update_enemies(self):
        """Update each enemy's movement and remove dead or finished enemies."""
        for enemy in self.enemies:
            enemy.update(self)

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
                        if bullet.tile_splash_radius > 0:
                            for enemy in self.enemies:
                                splash_radius = bullet.tile_splash_radius * config.GRID_CELL_SIZE
                                if bullet.x_pos-enemy.position[0] <= splash_radius or bullet.y_pos-enemy.position[1] <= splash_radius:
                                    enemy.take_damage(tower.bullet_damage, damage_type=bullet.type)
                        else:
                            enemy.take_damage(tower.bullet_damage, damage_type=bullet.type)
                                
                        bullet.active = False  # Mark bullet as inactive after hitting an enemy

    def check_game_over(self):
        if self.health <= 0:
            self.game.state_manager.change_state("Menu_State")
            self.game.state_manager.states["Menu_State"].change_menu("GameOverMenu")

    def check_win(self):
        if not self.wave_manager.wave_ongoing:
            if self.wave_manager.wave_number == GAME_DATA[self.difficulty]["Last Wave"]:
                self.game.state_manager.change_state("Menu_State")
                self.game.state_manager.states["Menu_State"].change_menu("WinMenu")

    def draw(self, screen):
        """
        Handles rendering the game to the screen.

        Args:
            screen: pygame display surface
        """
        self.map.draw(screen, self.mouse.map_grid_x, self.mouse.map_grid_y)  # Draw the game map
        self.draw_towers(screen)  # Draw all towers
        self.draw_enemies(screen)  # Draw all enemies
        self.highlight_selected_tower(screen) # Draw Highlight for selection AFTER drawing tower for clarity
        self.gamebuttons.draw(screen)
        self.tower_selection_menu.draw(screen)
        self.draw_error_message(screen)

    def highlight_selected_tower(self, screen):
        if self.mouse.current_action == "Selected Tower":
            grid_x, grid_y = self.mouse.current_selection.x_grid_pos, self.mouse.current_selection.y_grid_pos
            self.map.map_grid.highlight_square(screen, grid_x, grid_y, colour=(0, 255, 255))

    def draw_towers(self, screen):
        """Draw all towers on the screen."""
        for _, tower in self.towers.items():
            tower.draw(screen)

    def draw_enemies(self, screen):
        """Draw all enemies on the screen."""
        for enemy in self.enemies:
            enemy.draw(screen)

    def draw_error_message(self, screen):
        if self.error_message_display_time > 0:
            if self.error_message != None:
                message_text = self.error_font.render(f"Error: {self.error_message}", True, (255, 0, 0))
                screen.blit(message_text, (0, (config.GRID_SIZE + config.SCREEN_TOPBAR_HEIGHT)//2))
                self.error_message_display_time -= 1
        else:
            self.error_message = None
            self.error_message_display_time = self.total_error_message_display_time


    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_clicked = False

                if self.mouse.current_action == "Placing Tower":
                    self.place_tower()
                    button_clicked = True

                for button in self.gamebuttons.buttons:
                    if button.is_hovered():
                        button.click()
                        button_clicked = True

                for button in self.tower_selection_menu.buttons:
                    if button.is_hovered():
                        button.click()
                        button_clicked = True

                if not button_clicked:
                    self.select_tile()

    def place_tower(self):
        """
        Places a tower on the map grid and adds the selected tower to the game_state tower dict
        """
        print("trying to place tower")
        if self.money >= self.mouse.current_selection(0,0).cost:
            if self.map.place_tower(self.mouse.map_grid_x, self.mouse.map_grid_y): # If able to place tower
                self.create_tower(self.mouse.current_selection, (self.mouse.map_grid_x, self.mouse.map_grid_y)) # Create new tower object
                self.money -= self.mouse.current_selection(0,0).cost # Removes the cost of the tower from money
                print(f"successfully placed tower, tower list is{self.towers}") # print dictionary of towers for debugging purposes
                self.mouse.change_current_action(None, None) # Reset mouse action and selection
            else:
                self.select_tile()
        else:
            if self.map.check_tile((self.mouse.map_grid_x, self.mouse.map_grid_y)) != "outside grid":
                self.error_message = "Not enough money to place tower"
                self.mouse.change_current_action(None, None)
            else:
                self.select_tile()

    def remove_tower(self): # If able to remove tower
        """
        Removes a tower on the map grid and removes the selected tower from the game_state tower dict
        """
        self.money += self.towers[(self.mouse.current_selection.x_grid_pos, self.mouse.current_selection.y_grid_pos)].value//2
        self.map.remove_tower(self.mouse.current_selection.x_grid_pos, self.mouse.current_selection.y_grid_pos)
        del self.towers[(self.mouse.current_selection.x_grid_pos, self.mouse.current_selection.y_grid_pos)] # Delete selected tower object (at selected map coordinate)
        print(f"successfully deleted tower, tower list is{self.towers}") # print dictionary of towers for debugging purposes
        self.mouse.change_current_action(None, None) # Reset mouse action and selection

    def upgrade_tower(self):
        result = self.mouse.current_selection.upgrade(self.money)
        if result[0]:
            self.money -= result[1]
        else:
            self.error_message = result[1]
                
    def select_tile(self):
        if (self.mouse.map_grid_x, self.mouse.map_grid_y) in self.towers:
            self.mouse.change_current_action("Selected Tower", self.towers[(self.mouse.map_grid_x, self.mouse.map_grid_y)])
            print(f"successfully selected tower {self.towers[(self.mouse.map_grid_x, self.mouse.map_grid_y)]}")
        else:
            self.mouse.change_current_action(None, None)
            print(f"successfully unselected")

    def create_enemy(self, enemy_name, **kwargs):
        if kwargs:
            start_position = kwargs["Start_Position"]
            enemy_path = kwargs["Path"]
        else:
            start_position = self.map.enemy_start_pos
            enemy_path = self.map.enemy_path
        print(f"created enemy {enemy_name}")
        enemy_class = ENEMY_CLASS_MAP.get(enemy_name)
        if enemy_class:
            self.enemies.append(enemy_class(start_position, enemy_path))
        
    def create_tower(self, tower, position):
        self.towers[(self.mouse.map_grid_x, self.mouse.map_grid_y)] = tower(*position)
