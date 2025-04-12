from UI.Buttons.button_class import Button
import pygame

class SpriteButton(Button):
    """
    A button that displays different sprites depending on its state (normal, hovered, clicked).
    """
    
    def __init__(self, position, action, width, height, sprite, hover_sprite, click_sprite, text=None, font=None):
        """
        Initializes the SpriteButton with its properties and sprite images.

        Args:
            position (tuple): The (x, y) position of the button on the screen.
            action (function): The function to be called when the button is clicked.
            width (int): The width of the button.
            height (int): The height of the button.
            sprite (pygame.Surface): The normal sprite to display.
            hover_sprite (pygame.Surface): The sprite to display when the button is hovered.
            click_sprite (pygame.Surface): The sprite to display when the button is clicked.
            text (str, optional): The text to display on the button (default is None).
            font (pygame.Font, optional): The font for the button's text (default is None).
        """
        # Call the parent class constructor to initialize basic button attributes
        super().__init__(position, action, width, height, text, font)
        
        # Store sprite images
        self.sprite = sprite
        self.hover_sprite = hover_sprite
        self.click_sprite = click_sprite

    def draw(self, screen):
        """
        Draws the button on the screen, displaying the appropriate sprite based on its current state.

        Args:
            screen (pygame.Surface): The screen surface where the button will be drawn.
        """
        # Check the button's state and draw the corresponding sprite
        if self.is_clicked:
            # Draw the clicked sprite if the button is clicked
            screen.blit(self.click_sprite, self.rect.topleft)
        elif self.is_hovered():
            # Draw the hover sprite if the mouse is over the button
            screen.blit(self.hover_sprite, self.rect.topleft)
        else:
            # Draw the normal sprite if the button is neither clicked nor hovered
            screen.blit(self.sprite, self.rect.topleft)
