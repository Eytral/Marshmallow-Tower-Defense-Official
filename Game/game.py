import pygame
from Constants import config
from States.state_manager import StateManager
from States.game_state import Game_State
from States.menu_state import Menu_State
from States.pause_state import Pause_State

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
        
        # Initialize the state manager and add different game states
        self.state_manager = StateManager() 
        self.state_manager.add_state("Menu_State", Menu_State(self))
        self.state_manager.add_state("Game_State", Game_State(self))
        self.state_manager.add_state("Pause_State", Pause_State(self))

        # Start the game in the main menu
        self.state_manager.change_state("Menu_State")


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

            # Update the current state based on user input
            self.state_manager.update(events)

            # Clear the screen (set background to black)
            self.screen.fill((0, 0, 0))

            # Draw the current state on the screen
            self.state_manager.draw(self.screen)

            # Refresh the display
            pygame.display.flip()

            # Limit the frame rate to 60 FPS
            self.clock.tick(config.FPS)
