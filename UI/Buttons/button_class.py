import pygame
from abc import ABC, abstractmethod

class Button(ABC):
    """
    Abstract base class for creating buttons in the game.
    This class defines the basic properties and functionality for a button,
    including handling events like hover and click, and rendering the button.
    """

    def __init__(self, position, action, width, height, text=None, font=None):
        """
        Initializes a new button with the specified properties.

        Args:
            position (tuple): The (x, y) position of the button on the screen.
            action (function): The function to be executed when the button is clicked.
            width (int): The width of the button.
            height (int): The height of the button.
            text (str, optional): The text to display on the button (default is None).
            font (pygame.font.Font, optional): The font used for the button's text (default is Arial, size 24).
        """
        self.text = text
        self.position = position
        self.width, self.height = width, height
        self.action = action
        self.rect = pygame.Rect(position[0], position[1], self.width, self.height)
        self.font = font or pygame.font.SysFont('Arial', 24)

        self.is_clicked = False  # Indicates if the button is clicked
        self.is_selected = False  # Indicates if the button is selected

    def is_hovered(self):
        """
        Checks if the mouse cursor is hovering over the button.

        Returns:
            bool: True if the mouse cursor is over the button, False otherwise.
        """
        return self.rect.collidepoint(pygame.mouse.get_pos())  # Checks if mouse position is within button bounds

    def click(self):
        """
        Executes the action associated with the button when clicked.

        This method triggers the action function provided during button initialization.
        If the action is not callable, an error message is printed.
        """
        if callable(self.action):
            self.action()  # Execute the associated action when clicked
        else:
            print("Action is not callable.")  # Print an error if the action is not callable

    def handle_event(self, event):
        """
        Handles mouse events for the button, including hover and click.

        Args:
            event (pygame.event.Event): The event to be processed (e.g., MOUSEBUTTONDOWN).
        """
        # If the mouse button is pressed and the button is hovered over, set the clicked state
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered():
            self.is_clicked = True
            self.click()  # Trigger the button action when clicked

        # If the mouse button is released, reset the clicked state
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_clicked = False  # Reset the clicked state after release

    @abstractmethod
    def draw(self, screen):
        """
        Abstract method to draw the button on the screen.
        This method must be implemented by subclasses to define how the button is rendered.

        Args:
            screen (pygame.Surface): The surface (screen) on which the button will be drawn.
        """
        pass
