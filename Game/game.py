import pygame
from Constants import config

class Game():
    """Manages the main game loop and window management."""

    def __init__(self):
        """
        Initializes the game, sets up the window, and manages states.
        """
        pygame.init()  # Initialize pygame library

        # Create the game window with dimensions from config
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Marsh Tower Defense")  # Set window title

        self.clock = pygame.time.Clock()  # Create a clock to manage frame rate
        self.running = True  # Controls the game loop execution

    def run(self):
        """
        Runs the main game loop, handling events, updating states,
        and rendering the game.
        """
        while self.running:
            # Get all user input events
            events = pygame.event.get()  

            # Check for quit event (window close button)
            for event in events:
                if event.type == pygame.QUIT:  
                    self.running = False  # Stop the game loop

            # Clear the screen (set background to black)
            self.screen.fill((0, 0, 0))

            # Refresh the display
            pygame.display.flip()

            # Limit the frame rate to 60 FPS
            self.clock.tick(config.FPS)
