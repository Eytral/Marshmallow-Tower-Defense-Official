from States.base_state import State
import pygame

class Menu_State(State):
    """Main menu engine - Manages the menu logic, events, and rendering"""

    def __init__(self, game):
        """
        Initializes the Menu_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        """
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
        pass  # Placeholder for rendering logic

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