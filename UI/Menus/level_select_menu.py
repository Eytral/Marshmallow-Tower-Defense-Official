from UI.Menus.base_menu import Menu
from Constants import config
from Game.Map.maps import MAP_DATA

class LevelSelectMenu(Menu):
    """
    LevelSelectMenu displays a list of available levels (maps) and a button to return to the main menu.
    """

    def __init__(self, game):
        """
        Initialize the level select menu with map buttons and a 'Main Menu' button.

        Args:
            game (Game): The game instance holding the state manager and other game elements.
        """
        try:
            button_data = []

            # Add a button for each map in MAP_DATA
            for map_name in MAP_DATA:
                button_data.append({
                    "Text": map_name,
                    "Action": lambda map_name=map_name: self.set_level(map_name)
                })

            # Add a button to return to the main menu
            button_data.append({
                "Text": "Main Menu",
                "Action": self.back_to_main_menu
            })

            # Apply button styling and positioning
            for index, button in enumerate(button_data):
                button["ButtonType"] = "RectangleButton"
                button["Y_Position"] = (
                    config.DEFAULT_MENU_BUTTON_Y_POSITION +
                    (config.DEFAULT_BUTTON_HEIGHT * config.DEFAULT_BUTTON_VERTICAL_OFFSET) * index
                )

            # Initialize the base Menu class with the title "Level Select"
            super().__init__(game, "Level Select", button_data)

        except Exception as e:
            # Log any errors that occur during initialization
            print(f"[ERROR] Failed to initialize LevelSelectMenu: {e}")

    def draw(self, screen):
        """
        Draw the level selection menu onto the screen.

        Args:
            screen: The Pygame surface to draw the menu on.
        """
        try:
            # Draw the title and buttons using the parent class's draw method
            super().draw(screen)
        except Exception as e:
            # Log any errors that occur during the drawing process
            print(f"[ERROR] Failed to draw LevelSelectMenu: {e}")

    # ACTIONS (called when the respective buttons are clicked)

    def set_level(self, level_name):
        """
        Set the selected level and switch to the game state.

        Args:
            level_name (str): The name of the selected level.
        """
        try:
            # Change the game state to "Game_State" with the selected level
            self.game.state_manager.change_state("Game_State", level_name)
            return level_name
        except Exception as e:
            # Log any errors that occur when setting the level
            print(f"[ERROR] Failed to set the level: {e}")

    def back_to_main_menu(self):
        """
        Return to the main menu.
        """
        try:
            # Change to the MainMenu
            self.game.state_manager.current_state.change_menu("MainMenu")
        except Exception as e:
            # Log any errors that occur when returning to the main menu
            print(f"[ERROR] Failed to return to main menu: {e}")
