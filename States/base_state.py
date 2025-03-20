from abc import ABC, abstractmethod
class State(ABC):

    """
    Abstract Base Class for all game states/screens.

    Attributes:
        game: Reference to the main game object, allowing access to shared resources.
    """

    def __init__(self, game):
        self.game = game

    @abstractmethod
    def update(self, events):
        """
        Update logic based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        pass

    @abstractmethod
    def draw(self, screen):
        """
        Drawing logic for state

        Args:  
            screen: pygame display surface
        """
        pass

    @abstractmethod
    def handle_events(self, events):
        """
        Takes and processes user input and events

        Args:
            events: list of pygame events
        """
        pass

    def enter(self, *args, **kwargs):
        """Called when the state is entered."""
        pass

    def exit(self, *args, **kwargs):
        """Called when the state is exited"""
        pass