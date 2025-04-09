import pygame
from Constants import config
from UI.Menus.base_menu import Menu
from Game.Core.game_data import GAME_DATA

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
        NEXT_WAVE_BUTTON_WIDTH, NEXT_WAVE_BUTTON_HEIGHT = 175, 50
        PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT = 175, 50

        # Create button data with text and corresponding action
        button_data = [
            {"Text": "Next Wave", 
             "Action": self.start_wave,
             "Dimensions": (NEXT_WAVE_BUTTON_WIDTH, NEXT_WAVE_BUTTON_HEIGHT),
             "Y_Position": config.SCREEN_HEIGHT - NEXT_WAVE_BUTTON_HEIGHT - config.SCREEN_TOPBAR_HEIGHT//4,
             "X_Position": config.SCREEN_WIDTH - NEXT_WAVE_BUTTON_WIDTH - 20},
            {"Text": "Pause",
             "Action": self.pause_game,
             "Dimensions": (PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT),
             "Y_Position": 20,
             "X_Position": config.SCREEN_WIDTH - PAUSE_BUTTON_WIDTH - 20}
        ]
        
        for index, button in enumerate(button_data):
            button["ButtonType"] = "RectangleButton"

        # Create buttons using the provided button data
        super().__init__(game, None, button_data)  # Call the parent class's constructor
        self.body_font = pygame.font.Font(None, 45)

    def draw(self, screen):
        """
        Draws the TowerSelectionMenu on the screen.

        Args:
            screen: The pygame display surface where the menu is drawn.
        """
        for button in self.buttons:
            button.draw(screen)  # Draw each button

        health_surface = self.body_font.render(f"Health: {self.game.state_manager.states["Game_State"].health}", True, (255, 255, 255))
        money_surface = self.body_font.render(f"Money: {self.game.state_manager.states["Game_State"].money}", True, (255, 255, 255))  # White color for title text
        wave_surface = self.body_font.render(f"Wave: {self.game.state_manager.states["Game_State"].wave_manager.wave_number}/{GAME_DATA[self.game.state_manager.current_state.difficulty]["Last Wave"]}", True, (255, 255, 255))  # White color for title text

        surface_list = [health_surface, money_surface, wave_surface]
        for i, surface in enumerate(surface_list):
            text_rect = surface.get_rect()  # Get the rect of the title text for positioning
            text_rect.center = (100+200*i, config.SCREEN_TOPBAR_HEIGHT//2)  # Position the title at the center horizontally and near the top
            screen.blit(surface, text_rect)  # Draw the title on the screen
    
        if self.game.state_manager.current_state.wave_manager.wave_ongoing:
            text = "Ongoing..."
            colour = (255, 0, 0)
        else:
            text = "Ready"
            colour = (0, 255, 0)
        wave_ongoing_surface = self.body_font.render(text, True, colour)  # White color for title text
        text_rect = wave_ongoing_surface.get_rect()  # Get the rect of the title text for positioning
        text_rect.center = (700, config.SCREEN_TOPBAR_HEIGHT//2)  # Position the title at the center horizontally and near the top
        screen.blit(wave_ongoing_surface, text_rect)  # Draw the title on the screen



    def start_wave(self):
        """
        Starts the next game enemy wave
        """
        self.game.state_manager.current_state.wave_manager.next_wave()
        pass

    def pause_game(self):
        """
        Allows the player to remove a tower.
        """
        self.game.state_manager.change_state("Pause_State", exiting_game=False)