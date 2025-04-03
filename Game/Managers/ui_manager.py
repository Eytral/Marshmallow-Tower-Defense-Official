from UI.Menus.in_game_menu import GameButtons
from UI.Menus.tower_selection_menu import TowerSelectionMenu
import pygame
from Constants import config

class UIManager():
    def __init__(self, game_state):
        self.game_state = game_state
        self.game_buttons = GameButtons(self.game_state.game)
        self.tower_selection_menu = TowerSelectionMenu(self.game_state.game)

        self.total_error_message_display_time = 100
        self.error_message_display_time = 0
        self.error_font = pygame.font.Font(None, 50)
        self.error_message = None

    def draw_error_message(self, screen):
        if self.error_message_display_time > 0:
            if self.error_message != None:
                message_text = self.error_font.render(f"Error: {self.error_message}", True, (255, 0, 0))
                screen.blit(message_text, (0, (config.GRID_SIZE + config.SCREEN_TOPBAR_HEIGHT)//2))
                self.error_message_display_time -= 1
        else:
            self.error_message = None
            self.error_message_display_time = self.total_error_message_display_time

    def draw(self, screen):
        self.draw_error_message(screen)
        self.game_buttons.draw(screen)
        self.tower_selection_menu.draw(screen)

    def select_tile(self):
        if (self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y) in self.game_state.tower_manager.towers:
            self.game_state.mouse.change_current_action("Selected Tower", self.game_state.tower_manager.towers[(self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y)])
            print(f"successfully selected tower {self.game_state.tower_manager.towers[(self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y)]}")
        else:
            self.game_state.mouse.change_current_action(None, None)
            print(f"successfully unselected")

    def highlight_selected_tower(self, screen):
        if self.game_state.mouse.current_action == "Selected Tower":
            grid_x, grid_y = self.game_state.mouse.current_selection.x_grid_pos, self.game_state.mouse.current_selection.y_grid_pos
            self.game_state.map.map_grid.highlight_square(screen, grid_x, grid_y, colour=(0, 255, 255))