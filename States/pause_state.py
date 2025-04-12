from States.base_state import State
from UI.Menus.pause_menu import PauseMenu
import pygame

class Pause_State(State):
    """
    PauseState - Manages the pause logic, events, and rendering.
    
    This state is triggered when the game is paused. It handles events like
    resuming the game, opening the main menu, or exiting the game.
    """

    def __init__(self, game):
        """
        Initializes the Pause_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        """
        super().__init__(game)  # Call the parent State class constructor
        self.menu = PauseMenu(self.game)  # Initialize the PauseMenu for rendering and interaction

    def update(self, events):
        """
        Updates the pause state based on player input.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        
        Handles user inputs (like button clicks) while the game is paused.
        """
        self.handle_events(events)  # Process player input and other events during pause state

    def draw(self, screen):
        """
        Handles rendering the pause state to the screen.
        
        Args:
            screen: pygame display surface where the game is rendered.
        
        Draws the pause menu to the screen.
        """
        self.menu.draw(screen)  # Render the PauseMenu (buttons, background, etc.)

    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        
        Checks for mouse clicks on buttons and triggers their actions.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse button clicks
                for button in self.menu.buttons:  # Iterate through the menu buttons
                    if button.is_hovered():  # Check if the mouse is over a button
                        button.click()  # Trigger the button's action
