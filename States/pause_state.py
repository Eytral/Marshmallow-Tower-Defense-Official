from States.base_state import State
from UI.Menus.pause_menu import PauseMenu
import pygame

class Pause_State(State):
    """PauseState - Manages the pause logic, events and rendering."""

    def __init__(self, game):
        """
        Initializes the Pause_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        """
        super().__init__(game)  # Call the parent State class constructor
        self.menu = PauseMenu(self.game)

    def update(self, events):
        """
        Updates the pause state based on player input.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        self.handle_events(events)  # Process player input and other events

    def draw(self, screen):
        """
        Handles rendering the pause state to the screen.

        Args:
            screen: pygame display surface
        """
        self.menu.draw(screen)
        pass  # Placeholder for rendering logic

    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.menu.buttons:
                    if button.is_hovered():
                        button.click()
        pass  # Placeholder for event handling logic