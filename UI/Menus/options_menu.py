from UI.Menus.base_menu import Menu
from Constants import config
import pygame

class OptionsMenu(Menu):
    def __init__(self, game):
        """
        Initialize the options menu with title font, button font, and buttons.

        Args:
            game: The game object that holds the state manager and other game elements.
        """
        button_data = [
            {"Text": "Main Menu",
             "Action": self.back_to_main_menu},
            {"Text": "Easy Difficulty",
              "Action": lambda: self.change_difficulty("Easy")},
            {"Text": "Normal Difficulty",
             "Action": lambda: self.change_difficulty("Normal")},
            {"Text": "Hard Difficulty",
             "Action": lambda: self.change_difficulty("Hard")},
            {"Text": "Practise",
             "Action": self.toggle_practise}
        ]
        for index, button in enumerate(button_data):
            button["ButtonType"] = "RectangleButton"
            button["Y_Position"] = config.DEFAULT_MENU_BUTTON_Y_POSITION + (config.DEFAULT_BUTTON_HEIGHT*config.DEFAULT_BUTTON_VERTICAL_OFFSET)*index

        super().__init__(game, "Options", button_data)  # Call the parent class's constructor
        self.title_font = pygame.font.Font(None, 74)  # Font for the title

    def draw(self, screen):
        """
        Draw the title and buttons on the screen.

        Args:
            screen: The Pygame surface to draw the menu on.
        """
        # Create and render the title text
        super().draw(screen)  # Call the draw method from the parent class to draw the buttons

        difficulty_surface = self.body_font.render(f"Difficulty: {self.game.state_manager.states["Game_State"].difficulty}", True, (255, 255, 255))  # White color for title text
        practise_surface = self.body_font.render(f"Practise is: {self.game.state_manager.states["Game_State"].practise}", True, (255, 255, 255))  # White color for title text

        surface_list = [difficulty_surface, practise_surface]

        for i, surface in enumerate(surface_list):
            text_rect = surface.get_rect()  # Get the rect of the title text for positioning
            text_rect.center = (config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT-100+50*i)  # Position the title at the center horizontally and near the bottom
            screen.blit(surface, text_rect)  # Draw the title on the screen

    # ACTIONS (called when the respective buttons are clicked)
    def back_to_main_menu(self):
        """
        Action to return to the main menu when 'Main Menu' button is clicked.
        This changes the current menu to the "MainMenu".
        """
        self.game.state_manager.current_state.change_menu("MainMenu")

    def change_difficulty(self, difficulty):
        self.game.state_manager.states["Game_State"].game_manager.change_difficulty(difficulty)

    def toggle_practise(self):
        self.game.state_manager.states["Game_State"].game_manager.toggle_practise()