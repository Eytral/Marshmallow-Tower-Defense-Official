from Game.Core.game_data import GAME_DATA

class GameManager():
    """
    Manages the game state, including difficulty, practice mode, and win/lose conditions.
    """
    def __init__(self, game_state):
        """
        Initializes the GameManager with the given game state.
        
        Args:
            game_state: The current state of the game, which contains all game data.
        """
        self.game_state = game_state

    def change_difficulty(self, difficulty):
        """
        Changes the game's difficulty level and updates the relevant game stats.

        Args:
            difficulty (str): The new difficulty level to set (e.g., 'easy', 'medium', 'hard').
        """
        self.game_state.difficulty = difficulty  # Update the game state's difficulty
        self.game_state.wave_manager.difficulty = difficulty  # Update the wave manager's difficulty

        if not self.game_state.practise:
            # If not in practice mode, set the starting health and money based on the difficulty
            self.game_state.starting_health = GAME_DATA[difficulty]["Game_Stats"]["Starting Health"]
            self.game_state.starting_money = GAME_DATA[difficulty]["Game_Stats"]["Starting Money"]
        print(f"Successfully changed difficulty to {difficulty}")

    def toggle_practise(self):
        """
        Toggles the practice mode on or off. In practice mode, health and money are unlimited.

        Changes the starting health and money accordingly based on the mode.
        """
        if self.game_state.practise:
            self.game_state.practise = False  # Turn off practice mode
            # Set starting health and money based on the current difficulty
            self.game_state.starting_health = GAME_DATA[self.game_state.difficulty]["Game_Stats"]["Starting Health"]
            self.game_state.starting_money = GAME_DATA[self.game_state.difficulty]["Game_Stats"]["Starting Money"]
        else:
            self.game_state.practise = True  # Turn on practice mode
            # Set health and money to unlimited values in practice mode
            self.game_state.starting_health = 9999
            self.game_state.starting_money = 9999
        print(f"Successfully toggled practice mode to: {self.game_state.practise}")
    
    def check_game_over(self):
        """
        Checks if the game is over (health <= 0). If the game is over, transition to the game over menu.
        """
        if self.game_state.health <= 0:
            self.game_state.game.state_manager.change_state("Menu_State")  # Change to the menu state
            self.game_state.game.state_manager.states["Menu_State"].change_menu("GameOverMenu")  # Show the game over menu

    def check_win(self):
        """
        Checks if the player has won the game (last wave completed). If so, transition to the win menu.
        """
        if not self.game_state.wave_manager.wave_ongoing:
            if self.game_state.health > 0:
                # If the current wave is the last wave of the selected difficulty
                if self.game_state.wave_manager.wave_number == GAME_DATA[self.game_state.difficulty]["Last Wave"]:
                    self.game_state.game.state_manager.change_state("Menu_State")  # Change to the menu state
                    self.game_state.game.state_manager.states["Menu_State"].change_menu("WinMenu")  # Show the win menu
