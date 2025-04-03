# Import Parent Class
from States.base_state import State 

# Import Game Data
from Constants import config
from Game.Core.game_data import GAME_DATA

# Import Map
from Game.Map.map import Map 

# Import Managers
from Game.Managers.mouse import Mouse
from Game.Managers.wave_manager import WaveManager
from Game.Managers.bullet_manager import BulletManager
from Game.Managers.enemy_manager import EnemyManager
from Game.Managers.tower_manager import TowerManager
from Game.Managers.ui_manager import UIManager
from Game.Managers.game_manager import GameManager


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
        
        # Managers
        self.tower_manager = TowerManager(self)
        self.bullet_manager = BulletManager(self)
        self.enemy_manager = EnemyManager(self)
        self.wave_manager = WaveManager(self)
        self.ui_manager = UIManager(self)
        self.game_manager = GameManager(self)
        self.mouse = Mouse()

        self.difficulty = "Normal"
        self.starting_money = GAME_DATA[self.difficulty]["Game_Stats"]["Starting Money"]
        self.money = self.starting_money
        self.starting_health = GAME_DATA[self.difficulty]["Game_Stats"]["Starting Health"]
        self.health = self.starting_health

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
            self.enemy_manager.enemies = []
            self.tower_manager.towers = {}
            self.bullet_manager.bullets = []
            self.mouse.change_current_action(None, None)
            print("Game successfully exited")

    def update(self, events):
        """
        Updates the game based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        for button in self.ui_manager.tower_selection_menu.buttons:
            if button.is_hovered():
                self.mouse.currently_hovering = button.text
            
        self.mouse.update_mouse_pos()
        self.enemy_manager.update_enemies()  # Update enemy positions and check for removals
        self.tower_manager.update_towers()   # Update tower behavior (attacking, targeting, etc.)
        self.bullet_manager.check_bullet_collisions()  # Check and handle bullet collisions with enemies
        self.wave_manager.update()
        self.game_manager.check_game_over()
        self.game_manager.check_win()
        self.handle_events(events)  # Process player input and other events

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
                    self.tower_manager.place_tower()
                    button_clicked = True

                for button in self.ui_manager.game_buttons.buttons:
                    if button.is_hovered():
                        button.click()
                        button_clicked = True

                for button in self.ui_manager.tower_selection_menu.buttons:
                    if button.is_hovered():
                        button.click()
                        button_clicked = True

                if not button_clicked:
                    self.ui_manager.select_tile()

    def draw(self, screen):
        """
        Handles rendering the game to the screen.

        Args:
            screen: pygame display surface
        """
        self.map.draw(screen, self.mouse.map_grid_x, self.mouse.map_grid_y, )  # Draw the game map

        self.tower_manager.draw(screen)
        self.bullet_manager.draw(screen)
        self.enemy_manager.draw(screen)
        self.ui_manager.draw(screen)

        self.ui_manager.highlight_selected_tower(screen) # Draw Highlight for selection AFTER drawing tower for clarity
