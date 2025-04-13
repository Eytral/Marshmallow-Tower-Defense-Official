# Import Parent Class
from States.base_state import State 

# Import Game Data
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
    """Main game engine - Manages the in-game logic, events, and rendering.
    
    This class handles all the game mechanics such as updating enemies, towers, bullets, and checking win/loss conditions.
    It also processes user input and manages the game state transition.
    """

    def __init__(self, game):
        """
        Initializes the Game_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        
        Initializes the game map, managers, game stats (money, health, difficulty), and sets up the game.
        """
        super().__init__(game)  # Call the parent State class constructor

        # Initialize game map
        self.map = Map("Demonstration_Map")  # Stub/demonstration map
        
        # Initialize all game managers responsible for specific components
        self.tower_manager = TowerManager(self)
        self.bullet_manager = BulletManager(self)
        self.enemy_manager = EnemyManager(self)
        self.wave_manager = WaveManager(self)
        self.ui_manager = UIManager(self)
        self.game_manager = GameManager(self)
        self.mouse = Mouse()

        # Set default game settings based on difficulty
        self.difficulty = "Normal"
        self.practise = False
        self.starting_money = GAME_DATA[self.difficulty]["Game_Stats"]["Starting Money"]
        self.money = self.starting_money
        self.starting_health = GAME_DATA[self.difficulty]["Game_Stats"]["Starting Health"]
        self.health = self.starting_health

    def enter(self, *args):
        """
        Enters the Game_state, setting the level that will be played, and calling the load level function to load such level.

        Args:
            level_number: integer number representing the level that is being loaded
        
        Initializes or resets the game state when entering the Game State.
        """
        if args:
            level_name = args[0]
            self.map = Map(level_name)  # Load the map based on the provided level name
            self.wave_manager.reset_waves() # Reset wave manager when entering a new level
            print(f"Entering level {level_name}")
            self.health = self.starting_health  # Reset health
            self.money = self.starting_money  # Reset money

    def exit(self, **kwargs):
        """
        Exits the current Game_state and resets the necessary elements for a fresh start.

        Args:
            exiting_game (bool): Flag indicating if the player is exiting the game
        """
        exiting_game = kwargs.get("exiting_game", True)
        if exiting_game:
            # Reset game elements to their initial states
            self.map.reset_map()  # Reset map
            self.enemy_manager.enemies = []  # Clear enemies
            self.tower_manager.towers = {}  # Clear towers
            self.bullet_manager.bullets = []  # Clear bullets
            self.mouse.change_current_action(None, None)  # Reset mouse actions
            print("Game successfully exited")

    def update(self, events):
        """
        Updates the game based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        
        Updates the enemies, towers, bullets, waves, and checks for game over or win conditions.
        """
        for button in self.ui_manager.tower_selection_menu.buttons:
            if button.is_hovered():
                self.mouse.currently_hovering = button.text  # Display tower type on hover
            
        self.mouse.update_mouse_pos()  # Update mouse position
        self.enemy_manager.update_enemies()  # Update enemy positions and check for removals
        self.tower_manager.update_towers()   # Update tower behavior (attacking, targeting, etc.)
        self.bullet_manager.check_bullet_collisions()  # Check and handle bullet collisions with enemies
        self.wave_manager.update()  # Update wave logic (spawning, progress)
        self.game_manager.check_game_over()  # Check for game over conditions
        self.game_manager.check_win()  # Check for win conditions
        self.handle_events(events)  # Process player input and other events

    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        
        Detects mouse clicks for placing towers, interacting with UI buttons, and selecting tiles.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button click
                    button_clicked = False

                    if self.mouse.current_action == "Placing Tower":
                        self.tower_manager.place_tower()  # Place tower if the action is placing a tower
                        button_clicked = True

                    # Check if any UI button is clicked
                    for button in self.ui_manager.game_buttons.buttons:
                        if button.is_hovered():
                            button.click()
                            button_clicked = True

                    # Check if any tower selection button is clicked
                    for button in self.ui_manager.tower_selection_menu.buttons:
                        if button.is_hovered():
                            button.click()
                            button_clicked = True

                    # If no button was clicked, select the tile
                    if not button_clicked:
                        self.ui_manager.select_tile()
                if event.button == 3:  # Right mouse button click
                    self.mouse.change_current_action(None, None)  # Cancel current mouse action

    def draw(self, screen):
        """
        Handles rendering the game to the screen.

        Args:
            screen: pygame display surface
        
        Draws the game map, towers, bullets, enemies, and UI elements on the screen.
        """
        self.map.draw(screen)  # Draw the game map
        self.tower_manager.draw(screen)  # Draw towers
        self.bullet_manager.draw(screen)  # Draw bullets
        self.enemy_manager.draw(screen)  # Draw enemies
        self.ui_manager.draw(screen)  # Draw UI elements
