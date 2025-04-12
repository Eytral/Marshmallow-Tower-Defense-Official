from UI.Menus.base_menu import Menu
from Constants import config
import pygame

class OptionsMenu(Menu):
    """
    OptionsMenu allows the player to change game settings, such as difficulty and practise mode.
    It also provides the option to return to the main menu.
    """

    def __init__(self, game):
        """
        Initialize the OptionsMenu with buttons for changing game settings.

        Args:
            game (Game): The main game instance used to access state management and other game elements.
        """
        try:
            # Define menu buttons and their actions
            button_data = [
                {"Text": "Main Menu", "Action": self.back_to_main_menu},
                {"Text": "Easy Difficulty", "Action": lambda: self.change_difficulty("Easy")},
                {"Text": "Normal Difficulty", "Action": lambda: self.change_difficulty("Normal")},
                {"Text": "Hard Difficulty", "Action": lambda: self.change_difficulty("Hard")},
                {"Text": "Practise", "Action": self.toggle_practise}
            ]

            # Add styling and position for each button
            for index, button in enumerate(button_data):
                button["ButtonType"] = "RectangleButton"
                button["Y_Position"] = (
                    config.DEFAULT_MENU_BUTTON_Y_POSITION +
                    (config.DEFAULT_BUTTON_HEIGHT * config.DEFAULT_BUTTON_VERTICAL_OFFSET) * index
                )

            # Initialize the base Menu class with button data
            super().__init__(game, "Options", button_data)
            self.title_font = pygame.font.Font(None, 74)  # Title font for the menu

        except Exception as e:
            # Log any errors that occur during initialization
            print(f"[ERROR] Failed to initialize OptionsMenu: {e}")

    def draw(self, screen):
        """
        Draw the options menu, including the title, buttons, and game settings (difficulty and practise mode).

        Args:
            screen: The Pygame surface to draw the menu on.
        """
        try:
            # Draw the title and buttons using the parent class's draw method
            super().draw(screen)

            # Get current difficulty and practise mode from the game state
            game_state = self.game.state_manager.states["Game_State"]
            difficulty_text = f"Difficulty: {game_state.difficulty}"
            practise_text = f"Practise is: {game_state.practise}"

            # Render them as text surfaces
            difficulty_surface = self.body_font.render(difficulty_text, True, (255, 255, 255))
            practise_surface = self.body_font.render(practise_text, True, (255, 255, 255))

            # Blit the text near the bottom of the screen
            surface_list = [difficulty_surface, practise_surface]
            for i, surface in enumerate(surface_list):
                text_rect = surface.get_rect()
                text_rect.center = (
                    config.SCREEN_WIDTH // 2,
                    config.SCREEN_HEIGHT - 100 + 50 * i
                )
                screen.blit(surface, text_rect)

        except Exception as e:
            # Handle and log any errors during the drawing process
            print(f"[ERROR] Failed to draw OptionsMenu: {e}")

    # ACTIONS (called when the respective buttons are clicked)

    def back_to_main_menu(self):
        """
        Return to the main menu when the 'Main Menu' button is clicked.
        """
        try:
            # Change the current menu to the 'MainMenu'
            self.game.state_manager.current_state.change_menu("MainMenu")
        except Exception as e:
            # Log any errors that occur when trying to return to the main menu
            print(f"[ERROR] Failed to return to main menu: {e}")

    def change_difficulty(self, difficulty):
        """
        Change the game difficulty when a difficulty option is selected.

        Args:
            difficulty: String value representing the desired difficulty level (e.g., "Easy", "Normal", "Hard").
        """
        try:
            # Change the difficulty in the game state
            self.game.state_manager.states["Game_State"].game_manager.change_difficulty(difficulty)
        except Exception as e:
            # Log any errors that occur when trying to change the difficulty
            print(f"[ERROR] Failed to change difficulty to {difficulty}: {e}")

    def toggle_practise(self):
        """
        Toggle the practise mode on or off when the 'Practise' button is clicked.
        """
        try:
            # Toggle the practise mode in the game state
            self.game.state_manager.states["Game_State"].game_manager.toggle_practise()
        except Exception as e:
            # Log any errors that occur when toggling the practise mode
            print(f"[ERROR] Failed to toggle practise mode: {e}")
