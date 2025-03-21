from States.base_state import State 
from Game.map import Map 
from Entities.Towers.Bird_Flamethrower_tower import BirdFlamethrower
from Entities.Towers.Bomb_tower import Bomb
from Entities.Towers.Laser_tower import Laser
from Entities.Towers.Saw_tower import Saw
from Entities.Towers.Turret_Tower import Turret

from Entities.Enemies.marshmallow_enemy import Marshmallow
from Entities.Enemies.cracker_enemy import Cracker
from Entities.Enemies.white_chocolate_enemy import WhiteChocolate
from Entities.Enemies.dark_chocolate_enemy import DarkChocolate
from Entities.Enemies.smore_enemy import Smore

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

        # Placeholder towers for testing/demonstration
        placeholder_towers = [
            (0, 0, BirdFlamethrower), 
            (8, 2, Bomb), 
            (6, 3, Laser), 
            (2, 3, Saw), 
            (9, 9, Turret)
        ]
        
        # Create towers from placeholder data
        for tower in placeholder_towers:
            self.create_tower(*tower)

        # Define path for enemy movement
        path = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9)]
        start_position = (4, 0)
        end_position = (4, 9)
        
        # Placeholder enemies for testing/demonstration
        placeholder_enemies = [
            (start_position, end_position, path, Marshmallow),
            (start_position, end_position, path, Cracker),
            (start_position, end_position, path, WhiteChocolate),
            (start_position, end_position, path, DarkChocolate),
            (start_position, end_position, path, Smore)
        ]
        
        # Create enemies from placeholder data
        for enemy in placeholder_enemies:
            self.create_enemy(*enemy)

    def update(self, events):
        """
        Updates the game based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        self.update_enemies()  # Update enemy positions and check for removals
        self.update_towers()   # Update tower behavior (attacking, targeting, etc.)
        self.check_bullet_collisions()  # Check and handle bullet collisions with enemies
        self.handle_events(events)  # Process player input and other events

    def update_enemies(self):
        """Update each enemy's movement and remove dead or finished enemies."""
        for enemy in self.enemies:
            enemy.update()
            if enemy.is_dead or enemy.reached_end:
                self.enemies.remove(enemy)  # Remove enemy if it's dead or reaches the end

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
        self.map.draw(screen)  # Draw the game map
        self.draw_towers(screen)  # Draw all towers
        self.draw_enemies(screen)  # Draw all enemies

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
        pass  # Placeholder for event handling logic

    def create_tower(self, grid_x_position, grid_y_position, tower_type):
        """
        Creates and places a tower on the map.
        
        Args:
            grid_x_position (int): X-coordinate on the grid.
            grid_y_position (int): Y-coordinate on the grid.
            tower_type (class): The class of the tower to be instantiated.
        """
        self.towers[(grid_x_position, grid_y_position)] = tower_type(grid_x_position, grid_y_position)
        self.map.place_tower(grid_x_position, grid_y_position)

    def create_enemy(self, start_position, end_position, path, enemy_type):
        """
        Creates and adds an enemy to the game.
        
        Args:
            start_position (tuple): The starting position of the enemy.
            end_position (tuple): The ending position of the enemy.
            path (list): The path the enemy follows.
            enemy_type (class): The class of the enemy to be instantiated.
        """
        self.enemies.append(enemy_type(start_position, end_position, path))
