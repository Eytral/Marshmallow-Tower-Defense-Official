import pygame
from UI.Menus.in_game_menu import GameButtons
from UI.Menus.tower_selection_menu import TowerSelectionMenu
from Constants import config

class UIManager:
    """
    Manages UI elements in the game
    """
    def __init__(self, game_state):
        """
        Initializes the UIManager class to manage all UI elements in the game.

        Args:
            game_state: A reference to the current game state object.
        """
        self.game_state = game_state
        self.game_buttons = GameButtons(self.game_state.game)
        self.tower_selection_menu = TowerSelectionMenu(self.game_state.game)

        # Error message display settings
        self.total_error_message_display_time = 100
        self.error_message_display_time = 0
        self.error_font = pygame.font.Font(None, 30)
        self.error_message = None

    def change_error_message(self, error_message):
        """
        Changes the error message to be displayed and resets the display time.

        Args:
            error_message: The message to be displayed as an error.
        """
        self.error_message = error_message
        self.error_message_display_time = self.total_error_message_display_time

    def draw_error_message(self, screen):
        """
        Draws the error message on the screen if it exists.

        Args:
            screen: The game screen where the error message will be rendered.
        """
        if self.error_message_display_time > 0:
            if self.error_message:
                message_text = self.error_font.render(f"Error: {self.error_message}", True, (255, 0, 0))
                screen.blit(message_text, (0, config.SCREEN_TOPBAR_HEIGHT - 20))
                self.error_message_display_time -= 1
        else:
            self.error_message = None

    def draw(self, screen):
        """
        Draws all the necessary UI elements onto the screen.

        Args:
            screen: The game screen to draw all UI elements on.
        """
        # Draw game buttons and tower selection menu
        self.game_buttons.draw(screen)
        self.tower_selection_menu.draw(screen)

        # Handle actions for placing or selecting towers
        if self.game_state.mouse.current_action == "Placing Tower":
            self.draw_tower_preview(screen)
        if self.game_state.mouse.current_action == "Selected Tower":
            self.game_state.mouse.current_selection.highlight_tower_range(screen)
            self.highlight_selected_tower(screen)

        # Draw the error message if applicable
        self.draw_error_message(screen)

    def draw_tower_preview(self, screen):
        """
        Draws a preview of the tower that is being placed on the grid.

        Args:
            screen: The game screen where the tower preview will be drawn.
        """
        if self.game_state.mouse.is_on_grid():
            tower = self.game_state.mouse.current_selection(self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y)
            self.draw_tower_range_and_preview(screen, tower)

    def draw_tower_range_and_preview(self, screen, tower):
        """
        Draws both the tower's range and the preview for placing the tower.

        Args:
            screen: The game screen where the tower's range and preview will be drawn.
            tower: The tower object being placed.
        """
        tower.highlight_tower_range(screen, 
            left=self.game_state.mouse.map_grid_x * config.GRID_CELL_SIZE - tower.range * config.GRID_CELL_SIZE,
            top=self.game_state.mouse.map_grid_y * config.GRID_CELL_SIZE - tower.range * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT)

        # Draw preview of the tower's placement area on the grid
        self.game_state.map.preview_tower_placement_square(screen, self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y)

    def select_tile(self):
        """
        Selects or deselects the tower under the mouse pointer depending on whether it's already selected.

        This method updates the mouse's current action and selection based on the tile clicked.
        """
        selected_tile = (self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y)
        if selected_tile in self.game_state.tower_manager.towers:
            selected_tower = self.game_state.tower_manager.towers[selected_tile]
            self.game_state.mouse.change_current_action("Selected Tower", selected_tower)
            print(f"Successfully selected tower {selected_tower}")
        else:
            self.game_state.mouse.change_current_action(None, None)
            print("Successfully unselected")

    def highlight_selected_tower(self, screen):
        """
        Highlights the selected tower on the grid.

        Args:
            screen: The game screen where the selected tower will be highlighted.
        """
        if self.game_state.mouse.current_action == "Selected Tower":
            grid_x, grid_y = self.game_state.mouse.current_selection.x_grid_pos, self.game_state.mouse.current_selection.y_grid_pos
            self.game_state.map.map_grid.highlight_square(screen, grid_x, grid_y, colour=(0, 255, 255))
