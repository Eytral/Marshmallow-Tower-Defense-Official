from UI.Buttons.button_class import Button
import pygame

class RectangleButton(Button):
    def __init__(self, position, action, width, height, text=None, font=None, normal_color=(50,50,50), hover_colour=(255,0,0), click_colour=(255, 255, 0)):
        super().__init__(position, action, width, height, text, font)
        self.colour = normal_color
        self.hover_colour = hover_colour
        self.click_colour = click_colour

    def draw(self, screen):
        color = self.hover_colour if self.is_hovered() else self.colour

        # Draw the button as a rectangle with the chosen color
        pygame.draw.rect(screen, color, self.rect)

        # Render the text in white and center it inside the button
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center

        # Blit the text onto the screen
        screen.blit(text_surface, text_rect)

