from States.base_state import State
import pygame
from Constants import config

class Menu_State(State):
    """Main menu engine - Manages the menu logic, events, and rendering"""

    def __init__(self, game):
        """
        Initializes the Menu_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        """
        self.title_font = pygame.font.Font(None, 74)  # Font for the title
        super().__init__(game)  # Call the parent State class constructor

    def update(self, events):
        """
        Updates the menu based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        self.handle_events(events)  # Process player input and other events

    def draw(self, screen):
        """
        Handles rendering the menu state to the screen.
        
        Args:
            screen: pygame display surface
        """
        title_surface = self.title_font.render("Press Enter to Start", True, (255, 255, 255))  # White color for title text
        text_rect = title_surface.get_rect()  # Get the rect of the title text for positioning
        text_rect.center = (config.SCREEN_WIDTH // 2, 150)  # Position the title at the center horizontally and near the top
        screen.blit(title_surface, text_rect)  # Draw the title on the screen
        

    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.state_manager.change_state("Game_State")