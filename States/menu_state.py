from States.base_state import State
import pygame
from Constants import config
from UI.Menus.main_menu import MainMenu
from UI.Menus.options_menu import OptionsMenu
from UI.Menus.level_select_menu import LevelSelectMenu
from UI.Menus.game_over_menu import GameOverMenu

class Menu_State(State):
    """Main menu engine - Manages the menu logic, events, and rendering"""

    def __init__(self, game):
        """
        Initializes the Menu_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        """
        super().__init__(game)  # Call the parent State class constructor

        self.menus = {
            "MainMenu": MainMenu(self.game),
            "OptionsMenu": OptionsMenu(self.game),
            "LevelSelectMenu": LevelSelectMenu(self.game),
            "GameOverMenu": GameOverMenu(self.game)
        }
        self.title_font = pygame.font.Font(None, 74)  # Font for the title

        # Start with the MainMenu
        self.change_menu("MainMenu")


    def update(self, events):
        """
        Updates the menu based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        self.handle_events(events)  # Process player input and other events

    def draw(self, screen):
        """
        Handles rendering the menu state to the screen.
        
        Args:
            screen: pygame display surface
        """
        self.current_menu.draw(screen)

    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.current_menu.buttons:
                    if button.is_hovered():
                        button.click()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.state_manager.change_state("Game_State")

    def change_menu(self, menu_name):
        """Switch to a different menu (MainMenu, OptionsMenu, etc.)"""
        if menu_name in self.menus:
            self.current_menu = self.menus[menu_name]