from abc import ABC, abstractmethod
from UI.Buttons.rectangle_button import RectangleButton
from UI.Buttons.sprite_button import SpriteButton
from Constants import config
import pygame

class Menu(ABC):
    """
    Abstract base class for a menu in the game. Manages the creation and interaction with menu buttons.
    """
    
    def __init__(self, game, title, button_data):
        """
        Initializes the menu with the game reference, title, and button data.
        
        Args:
            game (Game): Reference to the main game object, used to interact with the game state.
            title (str): The title to be displayed on the menu.
            button_data (list): List of dictionaries containing button data for creating buttons.
        """
        self.game = game  # Store the reference to the game object
        self.buttons = []  # Initialize the buttons list to hold all menu buttons
        self.title = title  # Set the menu title
        self.create_buttons(button_data)  # Create buttons based on input button data
        self.title_font = pygame.font.Font(None, 74)  # Define the font for the title text (size 74)
        self.body_font = pygame.font.Font(None, 37)  # Define the font for the body text (size 37)

    def draw(self, screen):
        """
        Draw the menu and its buttons on the screen.
        
        Args:
            screen (pygame.Surface): The surface on which to draw the menu.
        """
        # Draw all buttons on the screen
        for button in self.buttons:
            button.draw(screen)

        # Render and display the title if it is defined
        if self.title:
            title_surface = self.title_font.render(self.title, True, (255, 255, 255))  # White color for title text
            text_rect = title_surface.get_rect()  # Get the rectangle for the title text to position it
            text_rect.center = (config.SCREEN_WIDTH // 2, 150)  # Center the title horizontally, place it near the top
            screen.blit(title_surface, text_rect)  # Blit the title to the screen

    def add_button(self, button):
        """
        Add a new button to the menu.
        
        Args:
            button (Button): The button object to be added to the menu.
        """
        self.buttons.append(button)  # Append the new button to the buttons list

    def remove_button(self, button):
        """
        Remove a button from the menu if it exists.
        
        Args:
            button (Button): The button object to be removed from the menu.
        """
        if button in self.buttons:
            self.buttons.remove(button)  # Remove the button from the list if it exists

    def create_buttons(self, button_data):
        """
        Create buttons from the provided button data and add them to the menu.
        
        Args:
            button_data (list): List of dictionaries containing data for each button.
        """
        for button in button_data:
            try:
                # Retrieve button data and set defaults if not provided
                button_type = button.get("ButtonType")
                action = button.get("Action")
                width, height = button.get("Dimensions", (config.DEFAULT_BUTTON_WIDTH, config.DEFAULT_BUTTON_HEIGHT))
                position_x = button.get("X_Position", config.SCREEN_WIDTH // 2 - width // 2)
                position_y = button.get("Y_Position")
                text = button.get("Text", None)
                font = button.get("Font", None)

                if button_type == "RectangleButton":
                    # Set default button colors
                    normal_color = button.get("Normal_Colour", (50, 50, 50))  # Default to grey
                    hover_colour = button.get("Hover_Colour", (255, 0, 0))  # Default to red
                    click_colour = button.get("Clicked_Colour", (0, 0, 255))  # Default to blue

                    # Create RectangleButton with specified properties
                    button = RectangleButton((position_x, position_y), action, width, height, normal_color, hover_colour, click_colour, text=text, font=font)

                elif button_type == "SpriteButton":
                    # Create SpriteButton with sprite properties
                    sprite = button.get("Sprite")
                    hover_sprite = button.get("Hover_Sprite")
                    clicked_sprite = button.get("Clicked_Sprite")
                    button = SpriteButton((position_x, position_y), action, width, height, sprite, hover_sprite, clicked_sprite, font=font)

                # Add the created button to the list of buttons if it was successfully created
                if button:
                    self.buttons.append(button)

            except KeyError as e:
                # Log missing required key in button data
                print(f"Error: Missing required key {e} in button data.")

            except Exception as e:
                # Log any unexpected errors during button creation
                print(f"An unexpected error occurred: {e}")
