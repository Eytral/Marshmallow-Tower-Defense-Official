import pygame
from Constants import config
from UI.Menus.base_menu import Menu

class GameButtons(Menu):
    """
    In game buttons

    Attributes:
        buttons: List of Button objects representing different game options.
        game: Reference to the main game object, used to interact with the game's current state.
    """

    def __init__(self, game):
        """
        Initializes the Game Menu

        Args:
            game: Reference to the main game object, used to manage the current state and mouse actions.
        """
        self.buttons = []  # List to store buttons for selecting towers
        self.game = game  # Game reference to interact with the game state

        # Create button data with text and corresponding action
        button_data = [
            {"Text": "Next Wave", 
             "Action": self.start_wave},
            {"Text": "Pause",
             "Action": self.pause_game}
        ]
        
        for index, button in enumerate(button_data):
            button["ButtonType"] = "RectangleButton"
            button["Dimensions"] = (100, 50)
            button["Y_Position"] = config.SCREEN_TOPBAR_HEIGHT//4
            button["X_Position"] = 220 + button["Dimensions"][0]*(config.DEFAULT_BUTTON_HORIZONTAL_OFFSET*index)

        # Create buttons using the provided button data
        super().__init__(game, None, button_data)  # Call the parent class's constructor
        self.body_font = pygame.font.Font(None, 20)

    def draw(self, screen):
        """
        Draws the TowerSelectionMenu on the screen.

        Args:
            screen: The pygame display surface where the menu is drawn.
        """
        for button in self.buttons:
            button.draw(screen)  # Draw each button
        
        health_surface = self.body_font.render(f"Health: {self.game.state_manager.states["Game_State"].health}", True, (255, 255, 255))  # White color for title text
        text_rect = health_surface.get_rect()  # Get the rect of the title text for positioning
        text_rect.center = (50, config.SCREEN_TOPBAR_HEIGHT//4)  # Position the title at the center horizontally and near the top
        screen.blit(health_surface, text_rect)  # Draw the title on the screen

        money_surface = self.body_font.render(f"Money: {self.game.state_manager.states["Game_State"].money}", True, (255, 255, 255))  # White color for title text
        text_rect = money_surface.get_rect()  # Get the rect of the title text for positioning
        text_rect.center = (50, config.SCREEN_TOPBAR_HEIGHT//4*2)  # Position the title at the center horizontally and near the top
        screen.blit(money_surface, text_rect)  # Draw the title on the screen
        

    def start_wave(self):
        """
        Starts the next game enemy wave
        """
        # Start next wave
        pass

    def pause_game(self):
        """
        Allows the player to remove a tower.
        """
        self.game.state_manager.change_state("Pause_State", exiting_game=False)
