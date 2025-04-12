from UI.Menus.base_menu import Menu
from Constants import config

class PauseMenu(Menu):
    """
    PauseMenu is displayed when the game is paused. It provides options to resume, return to the main menu, or exit the game.
    """

    def __init__(self, game):
        """
        Initialize the PauseMenu with the necessary button data, including their positions and actions.

        Args:
            game (Game): The main game instance used to access state management and other game elements.
        """
        try:
            # Define the buttons for the pause menu
            button_data = [
                {"Text": "Resume", "Action": self.resume_game},
                {"Text": "Main Menu", "Action": self.back_to_main_menu},
                {"Text": "Exit", "Action": self.exit_game}
            ]

            # Add layout metadata to each button
            for index, button in enumerate(button_data):
                button["ButtonType"] = "RectangleButton"
                button["Y_Position"] = (
                    config.DEFAULT_MENU_BUTTON_Y_POSITION +
                    (config.DEFAULT_BUTTON_HEIGHT * config.DEFAULT_BUTTON_VERTICAL_OFFSET) * index
                )

            # Initialize the parent Menu class with the button data
            super().__init__(game, "Pause", button_data)

        except Exception as e:
            # Catch any exceptions that occur during the initialization of the PauseMenu and log them
            print(f"[ERROR] Failed to initialize PauseMenu: {e}")

    def draw(self, screen):
        """
        Draw the pause menu, including the title and buttons, on the screen.

        Args:
            screen: The Pygame surface where the menu will be drawn.
        """
        try:
            # Draw the title and buttons using the base menu's draw method
            super().draw(screen)

            # Safely access values from the game state
            game_state = self.game.state_manager.states["Game_State"]
            difficulty_text = f"Difficulty: {game_state.difficulty}"
            practise_text = f"Practise is: {game_state.practise}"

            # Render the difficulty and practice mode info as text surfaces
            difficulty_surface = self.body_font.render(difficulty_text, True, (255, 255, 255))
            practise_surface = self.body_font.render(practise_text, True, (255, 255, 255))

            # Display them near the bottom of the screen
            surface_list = [difficulty_surface, practise_surface]
            for i, surface in enumerate(surface_list):
                text_rect = surface.get_rect()
                text_rect.center = (
                    config.SCREEN_WIDTH // 2,
                    config.SCREEN_HEIGHT - 100 + 50 * i
                )
                screen.blit(surface, text_rect)

        except Exception as e:
            # Handle any potential exceptions while drawing the menu
            print(f"[ERROR] Failed to draw PauseMenu: {e}")

    # ACTIONS (called when the respective buttons are clicked)
    def resume_game(self):
        """
        Action to resume the game when the 'Resume' button is clicked.
        """
        try:
            # Change the current state back to the game state (resumes gameplay)
            self.game.state_manager.change_state("Game_State")
        except Exception as e:
            # Log any errors that occur when trying to resume the game
            print(f"[ERROR] Failed to resume game: {e}")

    def back_to_main_menu(self):
        """
        Action to return to the main menu when the 'Main Menu' button is clicked.
        """
        try:
            # Exit the current game state (clean up if needed)
            self.game.state_manager.states["Game_State"].exit(exiting_game=True)
            # Switch to the menu state and change the current menu to the MainMenu
            self.game.state_manager.change_state("Menu_State")
            self.game.state_manager.current_state.change_menu("MainMenu")
        except Exception as e:
            # Log any errors that occur when trying to return to the main menu
            print(f"[ERROR] Failed to return to main menu: {e}")

    def exit_game(self):
        """
        Action to exit the game when the 'Exit' button is clicked.
        """
        try:
            # Set the game running state to False, which will stop the game loop
            self.game.running = False
        except Exception as e:
            # Log any errors that occur when trying to exit the game
            print(f"[ERROR] Failed to exit game: {e}")
