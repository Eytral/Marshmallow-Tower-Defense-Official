import pygame
from abc import ABC, abstractmethod

class Button(ABC):
    def __init__(self, position, action, width, height, text=None, font=None):
        """
        Initialize the button with text, position, action, and appearance options.
        
        Attributes:
            text: The text to display on the button.
            position: The (x, y) position to place the button on the screen.
            action: The function to call when the button is clicked.
            normal_color: The color of the button when not hovered (default: green).
            hover_color: The color of the button when hovered (default: yellow).
            font: The font to use for the button text (default: Arial, 24).
        """
        self.text = text
        self.position = position
        self.width, self.height = width, height
        self.action = action
        self.rect = pygame.Rect(position[0], position[1], self.width, self.height)
        # Use the provided font or fall back to a default font
        self.font = font or pygame.font.SysFont('Arial', 24)

        self.is_clicked = False
        self.is_selected = False

    def is_hovered(self):
        """
        Check if the mouse cursor is hovering over the button.

        Args:
            mouse_pos: The current position of the mouse (x, y).
        """
        return self.rect.collidepoint(pygame.mouse.get_pos()) #Returns True if the mouse is hovering over the button, False otherwise.

    def click(self):
        """
        Call the action function associated with the button when clicked.
        """
        self.action() # Call the action function associated with the button when clicked.

    @abstractmethod
    def draw(self, screen):
        """
        Draw the button on the screen with the appropriate color and text.
        
        Args:
            screen: The Pygame surface where the button will be drawn.
        """