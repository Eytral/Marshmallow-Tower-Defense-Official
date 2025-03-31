import pygame
from Constants import config
from Entities.Towers.base_tower import Tower
from UI.Menus.base_menu import Menu

class TowerSelectionMenu(Menu):
    """
    A menu for selecting a tower to place or remove.

    Attributes:
        title: The title of the menu displayed at the top.
        buttons: List of Button objects representing different tower options and removal.
        game: Reference to the main game object, used to interact with the game's current state.
        title_font: Font object used for rendering the title text.
    """

    def __init__(self, game):
        """
        Initializes the TowerSelectionMenu with the given game object.

        Args:
            game: Reference to the main game object, used to manage the current state and mouse actions.
        """
        self.title = "Select a Tower"  # Title of the menu
        self.buttons = []  # List to store buttons for selecting towers
        self.game = game  # Game reference to interact with the game state
        self.title_font = pygame.font.Font(None, 34)  # Font for the title text

        TOWER_BUTTON_WIDTH, TOWER_BUTTON_HEIGHT = 200, 60

        # Create button data with text and corresponding action
        button_data = []
        for tower_type in Tower.__subclasses__():
            button_data.append(
                {"Text": tower_type.__name__,
                                "Action": lambda t=tower_type: self.select_tower(t)}
                                )
            
        button_data.append({"Text": "Remove Tower",
                            "Action": self.remove_tower})  # Add remove tower button
        
        button_data.append({"Text": "Upgrade Tower",
                            "Action": self.upgrade_tower})  # Add remove tower button
                            
        
        for index, button in enumerate(button_data):
            button["ButtonType"] = "RectangleButton"
            button["Dimensions"] = TOWER_BUTTON_WIDTH, TOWER_BUTTON_HEIGHT
            button["X_Position"] = config.SCREEN_WIDTH - config.SCREEN_SIDEBAR_WIDTH + 25
            button["Y_Position"] = (config.SCREEN_TOPBAR_HEIGHT) + (button["Dimensions"][1]*config.DEFAULT_BUTTON_VERTICAL_OFFSET)*index

        # Create buttons using the provided button data
        super().__init__(game, None, button_data)  # Call the parent class's constructor

    def draw(self, screen):
        """
        Draws the TowerSelectionMenu on the screen.

        Args:
            screen: The pygame display surface where the menu is drawn.
        """
        for button in self.buttons:
            button.draw(screen)  # Draw each button

        # Render and draw the title of the menu
        title_surface = self.title_font.render(self.title, True, (255, 255, 255))  # White color for title text
        screen.blit(title_surface, (config.SCREEN_WIDTH - config.SCREEN_SIDEBAR_WIDTH, config.SCREEN_TOPBAR_HEIGHT // 2))  # Position the title

    def select_tower(self, tower_type):
        """
        Selects the tower type to place in the game.

        Args:
            tower_type: The type of tower to place, passed as a class reference (e.g., a subclass of Tower).
        """
        self.game.state_manager.current_state.mouse.change_current_action("Placing Tower", tower_type)

    def remove_tower(self):
        """
        Allows the player to remove a tower.
        """
        self.game.state_manager.current_state.mouse.change_current_action("Removing Tower", None)
        
    def upgrade_tower(self):
        """
        Allows the player to upgrade a tower.
        """
        self.game.state_manager.current_state.mouse.change_current_action("Upgrading Tower", None)

