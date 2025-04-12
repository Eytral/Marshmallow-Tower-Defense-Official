from abc import ABC, abstractmethod
import pygame

class State(ABC):
    """
    Abstract Base Class for all game states/screens.
    
    This class serves as a blueprint for other states in the game (e.g., MenuState, GameState).
    It defines common methods that all game states should implement.
    """

    def __init__(self, game):
        """
        Initializes the State with the provided game object.

        Args:
            game: Reference to the main game object, allowing access to shared resources.
        """
        self.game = game
        self.debug_font = pygame.font.Font(None, 25)  # Font for displaying debug information (FPS)

    @abstractmethod
    def update(self, events):
        """
        Update logic based on player input and game logic.

        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        
        This method should be implemented by subclasses to update the specific state.
        """
        pass

    @abstractmethod
    def draw(self, screen):
        """
        Drawing logic for the state.

        Args:
            screen: pygame display surface where the state will be drawn.
        
        This method should be implemented by subclasses to handle rendering.
        """
        pass

    @abstractmethod
    def handle_events(self, events):
        """
        Takes and processes user input and events.

        Args:
            events: List of pygame events such as key presses or mouse clicks.
        
        This method should be implemented by subclasses to handle state-specific events.
        """
        pass

    def enter(self, *args, **kwargs):
        """
        Called when the state is entered.

        This method can be overridden by subclasses if additional logic is needed when entering a state.
        
        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        pass

    def exit(self, *args, **kwargs):
        """
        Called when the state is exited.

        This method can be overridden by subclasses if additional logic is needed when exiting a state.
        
        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        pass

    def display_debug_info(self, screen, *args):
        """
        Displays debug information (e.g., FPS) on the screen.

        Args:
            screen: pygame display surface where the debug information will be displayed.
            *args: Additional arguments, the first should be FPS.
        
        The method displays the FPS on the top-left corner of the screen for debugging purposes.
        """
        fps = args[0]
        if fps:
            fps_text = self.debug_font.render(f"fps: {fps}", True, (255, 255, 255))
            screen.blit(fps_text, (0, 0))  # Draw FPS at the top-left corner of the screen
