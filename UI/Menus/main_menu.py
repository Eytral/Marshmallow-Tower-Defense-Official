from UI.Menus.base_menu import Menu
from Constants import config

class MainMenu(Menu):
    """
    MainMenu displays the primary menu where the player can start a new game, access options, or exit the game.
    """

    def __init__(self, game):
        """
        Initialize the main menu with buttons for starting the game, accessing options, or exiting.

        Args:
            game (Game): The main game instance that holds the state manager and other game elements.
        """
        try:
            # Define menu buttons and their respective actions
            button_data = [
                {"Text": "Start Game", "Action": self.start_game},
                {"Text": "Options", "Action": self.open_options},
                {"Text": "Exit", "Action": self.exit_game}
            ]

            # Set button appearance and vertical position for each button
            for index, button in enumerate(button_data):
                button["ButtonType"] = "RectangleButton"
                button["Y_Position"] = (
                    config.DEFAULT_MENU_BUTTON_Y_POSITION +
                    (config.DEFAULT_BUTTON_HEIGHT * config.DEFAULT_BUTTON_VERTICAL_OFFSET) * index
                )

            # Initialize the base Menu class with title "MainMenu"
            super().__init__(game, "Main Menu", button_data)

        except Exception as e:
            # Log any errors that occur during initialization
            print(f"[ERROR] Failed to initialize MainMenu: {e}")

    def draw(self, screen):
        """
        Draw the title and buttons on the screen.

        Args:
            screen: The Pygame surface to draw the menu on.
        """
        try:
            # Draw the title and buttons using the parent class's draw method
            super().draw(screen)
        except Exception as e:
            # Handle and log any errors during the drawing process
            print(f"[ERROR] Failed to draw MainMenu: {e}")

    # ACTIONS (called when the respective buttons are clicked)

    def start_game(self):
        """
        Start the game by switching to the level selection menu.
        """
        try:
            # Change to the LevelSelectMenu
            self.game.state_manager.current_state.change_menu("LevelSelectMenu")
        except Exception as e:
            # Log any errors that occur when trying to start the game
            print(f"[ERROR] Failed to start the game: {e}")

    def open_options(self):
        """
        Open the options menu to allow the player to modify game settings.
        """
        try:
            # Change to the OptionsMenu
            self.game.state_manager.current_state.change_menu("OptionsMenu")
        except Exception as e:
            # Log any errors that occur when trying to open the options menu
            print(f"[ERROR] Failed to open options menu: {e}")

    def exit_game(self):
        """
        Exit the game by setting the running flag to False, stopping the game loop.
        """
        try:
            # Stop the game loop by setting running to False
            self.game.running = False
        except Exception as e:
            # Log any errors that occur when trying to exit the game
            print(f"[ERROR] Failed to exit the game: {e}")
