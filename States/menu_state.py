from States.base_state import State
import pygame
from UI.Menus.main_menu import MainMenu
from UI.Menus.options_menu import OptionsMenu
from UI.Menus.level_select_menu import LevelSelectMenu
from UI.Menus.game_over_menu import GameOverMenu
from UI.Menus.win_menu import WinMenu


class Menu_State(State):
    """Main menu engine - Manages the menu logic, events, and rendering.
    
    This state handles different menu screens in the game, including the main menu, options menu,
    level select menu, game over menu, and win menu. It processes user input and updates the active menu.
    """

    def __init__(self, game):
        """
        Initializes the Menu_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        
        Initializes the menus dictionary with all available menus and starts with the MainMenu.
        """
        super().__init__(game)  # Call the parent State class constructor

        # Store all available menus
        self.menus = {
            "MainMenu": MainMenu(self.game),
            "OptionsMenu": OptionsMenu(self.game),
            "LevelSelectMenu": LevelSelectMenu(self.game),
            "GameOverMenu": GameOverMenu(self.game),
            "WinMenu": WinMenu(self.game)
        }
        self.title_font = pygame.font.Font(None, 74)  # Font for the title

        # Start with the MainMenu by default
        self.change_menu("MainMenu")


    def update(self, events):
        """
        Updates the menu based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        
        Processes player input and updates the state accordingly.
        """
        self.handle_events(events)  # Process player input and other events

    def draw(self, screen):
        """
        Handles rendering the menu state to the screen.
        
        Args:
            screen: pygame display surface.
        
        Draws the current active menu to the screen.
        """
        self.current_menu.draw(screen)

    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        
        Checks for mouse clicks on buttons and keyboard input (Enter key for transitioning to Game State).
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse button clicks
                for button in self.current_menu.buttons:  # Iterate through the current menu's buttons
                    if button.is_hovered():  # Check if the mouse is over a button
                        button.click()  # Trigger the button's action when clicked

            if event.type == pygame.KEYDOWN:  # Check for keyboard input
                if event.key == pygame.K_RETURN:  # Pressing Enter transitions to Game State
                    self.game.state_manager.change_state("Game_State")

    def change_menu(self, menu_name):
        """
        Switches to a different menu (MainMenu, OptionsMenu, etc.)
        
        Args:
            menu_name (str): The name of the menu to switch to (e.g., "MainMenu", "OptionsMenu").
        
        Sets the current menu to the specified menu.
        """
        if menu_name in self.menus:
            self.current_menu = self.menus[menu_name]  # Change to the specified menu
