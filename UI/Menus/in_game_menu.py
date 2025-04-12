import pygame
from Constants import config
from UI.Menus.base_menu import Menu
from Game.Core.game_data import GAME_DATA

class GameButtons(Menu):
    """
    In-game buttons for managing gameplay options such as starting waves and pausing the game.
    """
    def __init__(self, game):
        """
        Initializes the Game Menu with buttons for gameplay.

        Args:
            game (Game): Reference to the main game object, used to manage the current state and mouse actions.
        """
        try:
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

            # Apply button type for each button
            for index, button in enumerate(button_data):
                button["ButtonType"] = "RectangleButton"

            # Call the parent class's constructor to create buttons
            super().__init__(game, None, button_data)  # Initialize the base Menu class
            self.body_font = pygame.font.Font(None, 45)  # Set up font for rendering text

        except Exception as e:
            # Log any errors during initialization
            print(f"[ERROR] Failed to initialize GameButtons: {e}")

    def draw(self, screen):
        """
        Draws the game status and buttons on the screen.

        Args:
            screen: The pygame display surface where the menu is drawn.
        """
        try:
            # Draw each button in the button list
            for button in self.buttons:
                button.draw(screen)

            # Cache the game state to avoid multiple calls to the same data
            game_state = self.game.state_manager.states["Game_State"]

            # Render and display game stats: health, money, wave info
            health_surface = self.body_font.render(f"Health: {game_state.health}", True, (255, 255, 255))
            money_surface = self.body_font.render(f"Money: {game_state.money}", True, (255, 255, 255))
            wave_surface = self.body_font.render(
                f"Wave: {game_state.wave_manager.wave_number}/{GAME_DATA[game_state.difficulty]['Last Wave']}", 
                True, 
                (255, 255, 255)
            )

            # Draw game stats on the screen
            surface_list = [health_surface, money_surface, wave_surface]
            for i, surface in enumerate(surface_list):
                text_rect = surface.get_rect()
                text_rect.center = (100 + 200 * i, config.SCREEN_TOPBAR_HEIGHT // 2)
                screen.blit(surface, text_rect)
            
            # Display wave status: ongoing or ready
            wave_status = "Ongoing..." if game_state.wave_manager.wave_ongoing else "Ready"
            wave_color = (255, 0, 0) if game_state.wave_manager.wave_ongoing else (0, 255, 0)
            wave_ongoing_surface = self.body_font.render(wave_status, True, wave_color)
            
            # Position and draw wave status on screen
            text_rect = wave_ongoing_surface.get_rect()
            text_rect.center = (700, config.SCREEN_TOPBAR_HEIGHT // 2)
            screen.blit(wave_ongoing_surface, text_rect)

        except Exception as e:
            # Log any errors during the drawing process
            print(f"[ERROR] Failed to draw GameButtons: {e}")

    # ACTIONS (called when the respective buttons are clicked)

    def start_wave(self):
        """
        Starts the next enemy wave in the game.
        """
        try:
            # Trigger the start of the next wave in the game
            self.game.state_manager.current_state.wave_manager.next_wave()
        except Exception as e:
            # Log any errors when starting the wave
            print(f"[ERROR] Failed to start the wave: {e}")

    def pause_game(self):
        """
        Pauses the game and switches to the pause menu.
        """
        try:
            # Change to the Pause state to show the pause menu
            self.game.state_manager.change_state("Pause_State", exiting_game=False)
        except Exception as e:
            # Log any errors when pausing the game
            print(f"[ERROR] Failed to pause the game: {e}")
