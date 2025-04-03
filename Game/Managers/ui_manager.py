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