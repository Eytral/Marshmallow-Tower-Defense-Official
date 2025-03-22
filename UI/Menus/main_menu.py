from UI.Menus.base_menu import Menu
import pygame
from Constants import config
from UI.Buttons.rectangle_button import RectangleButton
from UI.Buttons.sprite_button import SpriteButton

class MainMenu(Menu):
    def __init__(self, game):
        """
        Initialize the main menu with title font, button font, and buttons.

        Args:
            game: The game object that holds the state manager and other game elements.
        """
        button_data = [
            {"Action": self.start_game,
            "Text": "Start Game"},
            {"Action": self.open_options,
            "Text": "Options"},
            {"Action": self.exit_game,
            "Text": "Exit"}]
        
        
        for index, button in enumerate(button_data):
            button["ButtonType"] = "RectangleButton"
            button["Y_Position"] = config.DEFAULT_MENU_BUTTON_Y_POSITION + (config.DEFAULT_BUTTON_HEIGHT*config.DEFAULT_BUTTON_VERTICAL_OFFSET)*index

        super().__init__(game, "MainMenu", button_data)  # Call the parent class's constructor

    def draw(self, screen):
        """
        Draw the title and buttons on the screen.

        Args:
            screen: The Pygame surface to draw the menu on.
        """
        super().draw(screen)
        # Create and render the title text

    # ACTIONS (called when the respective buttons are clicked)
    def start_game(self):
        """
        Action to switch to level select menu when clicking play game.
        """
        self.game.state_manager.current_state.change_menu("LevelSelectMenu")

    def open_options(self):
        """
        Action to open the options menu when 'Options' button is clicked.
        Updates the current menu to "OptionsMenu".
        """
        self.game.state_manager.current_state.change_menu("OptionsMenu")

    def exit_game(self):
        """
        Action to exit the game when 'Exit' button is clicked.
        Sets the game’s running state to False, which will stop the game loop.
        """
        self.game.running = False
