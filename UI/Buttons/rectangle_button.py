from UI.Buttons.button_class import Button
import pygame

class RectangleButton(Button):
    """
    A button that displays as a rectangle and changes colors based on its state (normal, hovered, clicked).
    """

    def __init__(self, position, action, width, height, normal_color, hover_colour, click_colour, text=None, font=None):
        """
        Initializes the RectangleButton with its properties, including color and text.

        Args:
            position (tuple): The (x, y) position of the button on the screen.
            action (function): The function to be called when the button is clicked.
            width (int): The width of the button.
            height (int): The height of the button.
            normal_color (tuple): The color of the button in its normal state.
            hover_colour (tuple): The color of the button when the mouse hovers over it.
            click_colour (tuple): The color of the button when it's clicked (selected).
            text (str, optional): The text to display on the button (default is None).
            font (pygame.Font, optional): The font for the button's text (default is None).
        """
        # Call the parent class constructor to initialize basic button attributes
        super().__init__(position, action, width, height, text, font)
        
        # Store color information for the different button states
        self.normal_colour = normal_color
        self.hover_colour = hover_colour
        self.click_colour = click_colour

    def draw(self, screen):
        """
        Draws the button on the screen, displaying the button in its current state (normal, hovered, clicked).

        Args:
            screen (pygame.Surface): The screen surface where the button will be drawn.
        """
        # Determine the button's current color based on whether it's selected, hovered, or in its normal state
        if self.is_selected:
            colour = self.click_colour  # If clicked, use the selected color
        elif self.is_hovered():
            colour = self.hover_colour  # If hovered, use the hover color
        else:
            colour = self.normal_colour  # In its normal state, use the normal color

        # Draw the button as a rectangle with the determined color
        pygame.draw.rect(screen, colour, self.rect)

        # Render the text and center it within the button if text is defined
        if self.text:
            # Create a text surface with the defined font and white color for text
            text_surface = self.font.render(self.text, True, (255, 255, 255))  
            text_rect = text_surface.get_rect()
            text_rect.center = self.rect.center  # Position the text at the center of the button
            screen.blit(text_surface, text_rect)  # Draw the text on the screen
