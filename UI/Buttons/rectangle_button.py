from UI.Buttons.button_class import Button
import pygame

class RectangleButton(Button):
    def __init__(self, position, action, width, height, normal_color, hover_colour, click_colour, text=None, font=None,):
        super().__init__(position, action, width, height, text, font)
        self.normal_colour = normal_color
        self.hover_colour = hover_colour
        self.click_colour = click_colour

    def draw(self, screen):
        colour = self.hover_colour if self.is_hovered() else self.normal_colour
        if self.is_selected:
            colour = self.click_colour

        # Draw the button as a rectangle with the chosen color
        pygame.draw.rect(screen, colour, self.rect)

        # Render the text in white and center it inside the button
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center

        # Blit the text onto the screen
        screen.blit(text_surface, text_rect)

