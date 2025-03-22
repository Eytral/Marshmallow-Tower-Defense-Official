from UI.Menus.base_menu import Menu
from UI.Menus.base_menu import Menu
from Constants import config
from Game.maps import MAP_DATA

class LevelSelectMenu(Menu):
    def __init__(self, game):
        """
        Initialize the options menu with title font, button font, and buttons.

        Args:
            game: The game object that holds the state manager and other game elements.
        """
        button_data = []
        for map_name in MAP_DATA:
            button_data.append(
                {"Text": map_name,
                "Action": lambda map_name=map_name: self.set_level(map_name)}
                )
            
        button_data.append(
            {"Text": "Main Menu",
            "Action": self.back_to_main_menu}
            )

        for index, button in enumerate(button_data):
            button["ButtonType"] = "RectangleButton"
            button["Y_Position"] = config.DEFAULT_MENU_BUTTON_Y_POSITION + (config.DEFAULT_BUTTON_HEIGHT*config.DEFAULT_BUTTON_VERTICAL_OFFSET)*index

        super().__init__(game, "Level Select", button_data)  # Call the parent class's constructor

    def draw(self, screen):
        """
        Draw the title and buttons on the screen.

        Args:
            screen: The Pygame surface to draw the menu on.
        """
        super().draw(screen)  # Call the draw method from the parent class to draw the buttons

    # ACTIONS (called when the respective buttons are clicked)
    def set_level(self, level_name):
        """
        Initialises the chosen level to play - sets the game state to "Game_state" and loads the level based on level_name

        Args:
            screen: The Pygame surface to draw the menu on.
        """
         
        self.game.state_manager.change_state("Game_State", level_name)
        return level_name
    
    def back_to_main_menu(self):
        """
        Action to return to the main menu when 'Main Menu' button is clicked.
        This changes the current menu to the "MainMenu".
        """
        self.game.state_manager.current_state.change_menu("MainMenu")
