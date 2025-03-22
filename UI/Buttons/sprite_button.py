from UI.Buttons.button_class import Button
import pygame

class SpriteButton(Button):
    def __init__(self, position, action, width, height, sprite, hover_sprite, click_sprite, text=None, font=None):
        super().__init__(position, action, width, height, text, font)
        self.sprite = sprite
        self.hover_sprite = hover_sprite
        self.click_sprite = click_sprite


    def draw(self, screen):
        """Draw a sprite-based button with hover effect."""
        if self.is_clicked:
            screen.blit(self.click_sprite, self.rect.topleft)
        if self.is_hovered():
            screen.blit(self.hover_sprite, self.rect.topleft)
        else:
            screen.blit(self.sprite, self.rect.topleft)