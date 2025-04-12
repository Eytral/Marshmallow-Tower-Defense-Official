from UI.Menus.base_menu import Menu
from Constants import config

class GameOverMenu(Menu):
    """
    Represents the Game Over menu with options to return to the main menu or exit the game.

    Attributes:
        game (Game): Reference to the main game object, used to manage the current state and interactions.
    """

    def __init__(self, game):
        """
        Initializes the Game Over menu with buttons for returning to the main menu or exiting the game.

        Args:
            game (Game): Reference to the main game object, used to manage the current state and interactions.
        """
        try:
            # Using a list instead of a tuple for flexibility (easy to add/remove buttons)
            button_data = [
                {"Text": "Back to Main Menu", "Action": self.back_to_main_menu},
                {"Text": "Exit", "Action": self.exit_game}
            ]
            
            # Loop through button data to initialize button attributes
            for index, button in enumerate(button_data):
                button["ButtonType"] = "RectangleButton"  # Define button type
                # Calculate Y position dynamically based on button height and offset
                button["Y_Position"] = config.DEFAULT_MENU_BUTTON_Y_POSITION + (config.DEFAULT_BUTTON_HEIGHT * config.DEFAULT_BUTTON_VERTICAL_OFFSET) * index

            # Call the parent class constructor to initialize the menu
            super().__init__(game, "Game Over", button_data)  # Initialize the base Menu class

        except Exception as e:
            # Log any initialization errors
            print(f"[ERROR] Failed to initialize GameOverMenu: {e}")

    def back_to_main_menu(self):
        """
        Action to return to the main menu when 'Main Menu' button is clicked.
        This changes the current menu to the "MainMenu".
        """
        try:
            # Ensure game state cleanup if needed before switching
            self.game.state_manager.states["Game_State"].exit(exiting_game=True)
            self.game.state_manager.change_state("Menu_State")  # Switch to Menu State
            self.game.state_manager.current_state.change_menu("MainMenu")  # Change to Main Menu
        except KeyError:
            # Log error if 'Game_State' does not exist in the state manager
            print("Error: 'Game_State' does not exist in state manager.")  # Added exception handling for missing game state
        except Exception as e:
            # Log other errors in this method
            print(f"[ERROR] Failed to return to the main menu: {e}")

    def exit_game(self):
        """
        Action to exit the game when 'Exit' button is clicked.
        Sets the game’s running state to False, which will stop the game loop.
        """
        try:
            # Set game running state to False to stop the game loop
            self.game.running = False
        except Exception as e:
            # Log any errors during the exit process
            print(f"[ERROR] Failed to exit the game: {e}")
