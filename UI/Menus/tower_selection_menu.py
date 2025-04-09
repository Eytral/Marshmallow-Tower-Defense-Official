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
        self.stat_font = pygame.font.Font(None, 20)

        self.TOWER_BUTTON_WIDTH, self.TOWER_BUTTON_HEIGHT = 200, 60
        self.TOWER_BUTTON_X_POSITION = config.SCREEN_WIDTH - config.SCREEN_SIDEBAR_WIDTH + 25

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
            button["Dimensions"] = self.TOWER_BUTTON_WIDTH, self.TOWER_BUTTON_HEIGHT
            button["X_Position"] = self.TOWER_BUTTON_X_POSITION
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
        mouse = self.game.state_manager.states["Game_State"].mouse

        for button in self.buttons:
            if mouse.current_action == "Placing Tower":
                if mouse.current_selection.__name__ == button.text:
                    button.is_selected = True
                else:
                    button.is_selected = False
            else:
                button.is_selected = False
        if mouse.current_selection != None:
            if mouse.current_action == "Selected Tower":
                tower = mouse.current_selection
                selected_tower = True
            else:
                tower = mouse.current_selection(0,0)
                selected_tower = False
            self.draw_tower_info(screen, tower, selected_tower)


    def draw_tower_info(self, screen, tower, selected_tower):
        # Initialize a dictionary to hold stats
        tower_stats = {}

        # Add the tower name as the first entry
        tower_stats["Name"] = tower.__class__.__name__

        # Add the cost of the tower
        if selected_tower:
            # For selected towers, cost is not relevant
            tower_stats["Value"] = tower.value
        else:
            # For unselected towers, show the cost
            tower_stats["Cost"] = tower.cost

        # Get the current upgrade level stats
        current_upgrade_stats = tower.tower_data[f"UPGRADE {tower.upgrade_level}"]

        # Add current stats to the dictionary (excluding "Cost" since it's already handled)
        for stat, value in current_upgrade_stats.items():
            if stat != "Cost":
                tower_stats[stat] = f"{value}"

        # Handle selected tower scenario
        if selected_tower:
            # Determine the next upgrade level
            next_upgrade_level = tower.upgrade_level + 1

            # Check if there's a next upgrade level
            if next_upgrade_level > len(tower.tower_data) - 1:
                # No more upgrades, mark stats as "MAX"
                for stat in current_upgrade_stats:
                    if stat != "Cost":
                        tower_stats[stat] += " (MAX)"
            else:
                # Add next upgrade stats
                next_upgrade_stats = tower.tower_data[f"UPGRADE {next_upgrade_level}"]
                for stat, next_value in next_upgrade_stats.items():
                    if stat != "Cost" and stat in tower_stats:
                        tower_stats[stat] += f" -> {next_value}"

        # Render and display the stats on the screen
        for index, (stat, value) in enumerate(tower_stats.items()):
            display_text = f"{stat}: {value}"
            body_surface = self.stat_font.render(display_text, True, (255, 255, 255))
            screen.blit(body_surface, (self.TOWER_BUTTON_X_POSITION + self.TOWER_BUTTON_WIDTH + 20, config.SCREEN_TOPBAR_HEIGHT + index * 20))

    def select_tower(self, tower_type):
        """
        Selects the tower type to place in the game.

        Args:
            tower_type: The type of tower to place, passed as a class reference (e.g., a subclass of Tower).
        """
        self.game.state_manager.states["Game_State"].mouse.change_current_action("Placing Tower", tower_type)

    def remove_tower(self):
        """
        Allows the player to remove a tower.
        """
        if self.game.state_manager.states["Game_State"].mouse.current_action == "Selected Tower":
            self.game.state_manager.states["Game_State"].tower_manager.remove_tower()
        
    def upgrade_tower(self):
        """
        Allows the player to upgrade a tower.
        """
        if self.game.state_manager.states["Game_State"].mouse.current_action == "Selected Tower":
            self.game.state_manager.states["Game_State"].tower_manager.upgrade_tower()

