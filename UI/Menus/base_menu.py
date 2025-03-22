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
            position = button["Position"]
            action = button["Action"]
            width, height = button["Dimensions"]
            text = button.get("Text", None)
            font = button.get("Font", None)

            # Create a dictionary of optional arguments
            optional_args = {}

            if button_type == "RectangleButton":
                # Add optional color attributes only if they exist
                if "Colour" in button:
                    optional_args["normal_colour"] = button["Colour"]
                if "Hover_Colour" in button:
                    optional_args["hover_colour"] = button["Hover_Colour"]
                if "Clicked_Colour" in button:
                    optional_args["clicked_colour"] = button["Clicked_Colour"]

                button = RectangleButton(position, action, width, height, text, font=font, **optional_args)
            
            elif button_type == "SpriteButton":
                sprite = button["Sprite"]
                hover_sprite = button["Hover_Sprite"]
                clicked_sprite = button["Clicked_Sprite"]
                button = SpriteButton(position, action, width, height, sprite, hover_sprite, clicked_sprite, font=font)

            self.buttons.append(button)

