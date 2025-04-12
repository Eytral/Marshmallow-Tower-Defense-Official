from UI.Menus.base_menu import Menu
from Constants import config

class WinMenu(Menu):
    """
    WinMenu displays a congratulatory message and provides the player
    with options to return to the main menu or exit the game.
    """

    def __init__(self, game):
        """
        Initialize the WinMenu with two buttons: 'Back to Main Menu' and 'Exit'.

        Args:
            game (Game): The main game instance used to access state management.
        """
        try:
            # Define the button data with 'Back to Main Menu' and 'Exit' options
            button_data = (
                {"Text": "Back to Main Menu", "Action": self.back_to_main_menu},
                {"Text": "Exit", "Action": self.exit_game}
            )

            # Add layout metadata to each button (positioning and button type)
            for index, button in enumerate(button_data):
                button["ButtonType"] = "RectangleButton"
                # Position buttons vertically with a gap based on configuration
                button["Y_Position"] = config.DEFAULT_MENU_BUTTON_Y_POSITION + \
                    (config.DEFAULT_BUTTON_HEIGHT * config.DEFAULT_BUTTON_VERTICAL_OFFSET) * index

            # Initialize parent Menu class with heading and buttons
            super().__init__(game, "You Win!", button_data)

        except Exception as e:
            # Catch and print errors if the WinMenu initialization fails
            print(f"[ERROR] Failed to initialize WinMenu: {e}")

    def back_to_main_menu(self):
        """
        Action to return to the main menu when 'Back to Main Menu' button is clicked.
        This changes the current menu to the 'MainMenu'.
        """
        try:
            # Exit the current game state and perform necessary cleanup
            self.game.state_manager.states["Game_State"].exit(exiting_game=True)
            # Switch to the Menu state
            self.game.state_manager.change_state("Menu_State")
            # Update the current menu to the main menu
            self.game.state_manager.current_state.change_menu("MainMenu")
        except Exception as e:
            # Catch and print errors if the transition to main menu fails
            print(f"[ERROR] Failed to return to main menu: {e}")

    def exit_game(self):
        """
        Action to exit the game when 'Exit' button is clicked.
        Sets the game’s running state to False, which will stop the game loop.
        """
        try:
            # Stop the game by setting the running state to False
            self.game.running = False
        except Exception as e:
            # Catch and print errors if exiting the game fails
            print(f"[ERROR] Failed to exit game: {e}")
