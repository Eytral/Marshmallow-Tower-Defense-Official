import pygame
from Constants import config
from Entities.Towers.base_tower import Tower
from UI.Menus.base_menu import Menu

class TowerSelectionMenu(Menu):
    """
    A menu for selecting a tower to place or remove.
    """

    def __init__(self, game):
        """
        Initializes the TowerSelectionMenu with buttons for placing, removing, and upgrading towers.

        Args:
            game (Game): Reference to the main game instance.
        """
        try:
            self.title = "Select a Tower"
            self.buttons = []
            self.game = game

            self.title_font = pygame.font.Font(None, 34)
            self.stat_font = pygame.font.Font(None, 20)

            self.TOWER_BUTTON_WIDTH, self.TOWER_BUTTON_HEIGHT = 200, 60
            self.TOWER_BUTTON_X_POSITION = config.SCREEN_WIDTH - config.SCREEN_SIDEBAR_WIDTH + 25

            button_data = []

            # Add a button for each tower subclass
            for tower_type in Tower.__subclasses__():
                button_data.append({
                    "Text": tower_type.__name__,
                    "Action": lambda t=tower_type: self.select_tower(t)
                })

            # Add sell and upgrade buttons
            button_data.append({"Text": "Sell Tower", "Action": self.remove_tower})
            button_data.append({"Text": "Upgrade Tower", "Action": self.upgrade_tower})

            # Assign position and styling attributes to each button
            for index, button in enumerate(button_data):
                button["ButtonType"] = "RectangleButton"
                button["Dimensions"] = self.TOWER_BUTTON_WIDTH, self.TOWER_BUTTON_HEIGHT
                button["X_Position"] = self.TOWER_BUTTON_X_POSITION
                button["Y_Position"] = (
                    config.SCREEN_TOPBAR_HEIGHT +
                    (button["Dimensions"][1] * config.DEFAULT_BUTTON_VERTICAL_OFFSET) * index
                )

            # Initialize the base menu with generated buttons
            super().__init__(game, None, button_data)

        except Exception as e:
            print(f"[ERROR] Failed to initialize TowerSelectionMenu: {e}")

    def draw(self, screen):
        """
        Draws the TowerSelectionMenu and highlights the selected tower button.

        Args:
            screen (pygame.Surface): The surface on which to draw the menu.
        """
        try:
            for button in self.buttons:
                button.draw(screen)

            # Render and display the menu title
            title_surface = self.title_font.render(self.title, True, (255, 255, 255))
            screen.blit(title_surface, (config.SCREEN_WIDTH - config.SCREEN_SIDEBAR_WIDTH, config.SCREEN_TOPBAR_HEIGHT // 2))

            mouse = self.game.state_manager.states["Game_State"].mouse

            # Highlight the button corresponding to the currently selected tower
            for button in self.buttons:
                if mouse.current_action == "Placing Tower":
                    button.is_selected = (mouse.current_selection.__name__ == button.text)
                else:
                    button.is_selected = False

            # Show tower information if a tower is selected or being placed
            if mouse.current_selection is not None:
                if mouse.current_action == "Selected Tower":
                    tower = mouse.current_selection
                    selected_tower = True
                else:
                    tower = mouse.current_selection(0, 0)  # Create preview
                    selected_tower = False

                self.draw_tower_info(screen, tower, selected_tower)

        except Exception as e:
            print(f"[ERROR] Failed to draw TowerSelectionMenu: {e}")

    def draw_tower_info(self, screen, tower, selected_tower):
        """
        Displays the tower's statistics and upgrade information.

        Args:
            screen (pygame.Surface): Surface to render the text on.
            tower (Tower): Tower instance to display info about.
            selected_tower (bool): Whether this is a selected tower (vs. a new placement).
        """
        try:
            tower_stats = {}
            tower_stats["Name"] = tower.__class__.__name__

            if selected_tower:
                # Show value and upgrade cost if applicable
                next_upgrade_level = tower.upgrade_level + 1
                if next_upgrade_level < len(tower.tower_data) - 1:
                    tower_stats["Upgrade Cost"] = tower.tower_data[f"UPGRADE {next_upgrade_level}"]["Cost"]
                tower_stats["Value"] = tower.value
            else:
                tower_stats["Cost"] = tower.cost

            current_upgrade_stats = tower.tower_data[f"UPGRADE {tower.upgrade_level}"]

            # Show current stats
            for stat, value in current_upgrade_stats.items():
                if stat != "Cost":
                    tower_stats[stat] = f"{value}"

            # Append upgrade info if selected
            if selected_tower:
                next_upgrade_level = tower.upgrade_level + 1
                if next_upgrade_level > len(tower.tower_data) - 1:
                    for stat in current_upgrade_stats:
                        if stat != "Cost":
                            tower_stats[stat] += " (MAX)"
                else:
                    next_upgrade_stats = tower.tower_data[f"UPGRADE {next_upgrade_level}"]
                    for stat, next_value in next_upgrade_stats.items():
                        if stat != "Cost" and stat in tower_stats:
                            tower_stats[stat] += f" -> {next_value}"

            # Display tower stats
            for index, (stat, value) in enumerate(tower_stats.items()):
                display_text = f"{stat}: {value}"
                body_surface = self.stat_font.render(display_text, True, (255, 255, 255))
                screen.blit(body_surface, (
                    self.TOWER_BUTTON_X_POSITION + self.TOWER_BUTTON_WIDTH + 20,
                    config.SCREEN_TOPBAR_HEIGHT + index * 20
                ))
        except Exception as e:
            print(f"[ERROR] Failed to draw tower info: {e}")

    def select_tower(self, tower_type):
        """
        Selects the tower type to place on the grid.

        Args:
            tower_type (class): Class of the tower to be placed.
        """
        try:
            self.game.state_manager.states["Game_State"].mouse.change_current_action("Placing Tower", tower_type)
        except Exception as e:
            print(f"[ERROR] Failed to select tower: {e}")

    def remove_tower(self):
        """
        Removes the currently selected tower from the game board.
        """
        try:
            if self.game.state_manager.states["Game_State"].mouse.current_action == "Selected Tower":
                self.game.state_manager.states["Game_State"].tower_manager.remove_tower()
        except Exception as e:
            print(f"[ERROR] Failed to remove tower: {e}")

    def upgrade_tower(self):
        """
        Upgrades the currently selected tower if possible.
        """
        try:
            if self.game.state_manager.states["Game_State"].mouse.current_action == "Selected Tower":
                self.game.state_manager.states["Game_State"].tower_manager.upgrade_tower()
        except Exception as e:
            print(f"[ERROR] Failed to upgrade tower: {e}")
