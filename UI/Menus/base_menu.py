from abc import ABC, abstractmethod
from UI.Buttons.rectangle_button import RectangleButton
from UI.Buttons.sprite_button import SpriteButton
from Constants import config
import pygame

class Menu(ABC):
    def __init__(self, game, title, button_data):
        self.game = game
        self.buttons = []
        self.title = title
        self.create_buttons(button_data)
        self.title_font = pygame.font.Font(None, 74)  # Font for the title
        self.body_font = pygame.font.Font(None, 37)  # Font for the title


    def draw(self, screen):
        """Draw the menu and its buttons."""
        for button in self.buttons:
            button.draw(screen)

        if self.title != None:
            title_surface = self.title_font.render(self.title, True, (255, 255, 255))  # White color for title text
            text_rect = title_surface.get_rect()  # Get the rect of the title text for positioning
            text_rect.center = (config.SCREEN_WIDTH // 2, 150)  # Position the title at the center horizontally and near the top
            screen.blit(title_surface, text_rect)  # Draw the title on the screen
            

    def add_button(self, button):
        """Add a button to the menu."""
        self.buttons.append(button)

    def create_buttons(self, button_data):
        for button in button_data:
            button_type = button["ButtonType"]
            action = button["Action"]
            width, height = button.get("Dimensions", (config.DEFAULT_BUTTON_WIDTH, config.DEFAULT_BUTTON_HEIGHT))
            position_x = button.get("X_Position", config.SCREEN_WIDTH//2 - width//2)
            position_y = button["Y_Position"]
            text = button.get("Text", None)
            font = button.get("Font", None)

            if button_type == "RectangleButton":
                # Add optional color attributes only if they exist
                normal_color = button.get("Normal_Colour", (50, 50, 50))
                hover_colour = button.get("Hover_Colour", (255, 0, 0))
                click_colour = button.get("Clicked_Colour", (255, 255, 0))

                button = RectangleButton((position_x, position_y), action, width, height, normal_color, hover_colour, click_colour, text=text, font=font)
            
            elif button_type == "SpriteButton":
                sprite = button["Sprite"]
                hover_sprite = button["Hover_Sprite"]
                clicked_sprite = button["Clicked_Sprite"]
                button = SpriteButton((position_x, position_y), action, width, height, sprite, hover_sprite, clicked_sprite, font=font)

            self.buttons.append(button)

