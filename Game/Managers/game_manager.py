from Game.Core.game_data import GAME_DATA

class GameManager():
    def __init__(self, game_state):
        self.game_state = game_state

    def change_difficulty(self, difficulty):
        self.game_state.difficulty = difficulty
        self.game_state.wave_manager.difficulty = difficulty
        self.game_state.starting_health = GAME_DATA[difficulty]["Game_Stats"]["Starting Health"]
        self.game_state.starting_money = GAME_DATA[difficulty]["Game_Stats"]["Starting Money"]
        print(f"Successfully changed difficuty to {difficulty}")

    def toggle_practise(self):
        if self.game_state.practise:
            self.game_state.practise = False
            self.game_state.starting_health = GAME_DATA[self.game_state.difficulty]["Game_Stats"]["Starting Health"]
            self.game_state.starting_money = GAME_DATA[self.game_state.difficulty]["Game_Stats"]["Starting Money"]
        else:
            self.game_state.practise = True
            self.game_state.starting_health = 9999
            self.game_state.starting_money = 9999
        print(f"Successfully toggle practise to: {self.game_state.practise}")
    
    def check_game_over(self):
        if self.game_state.health <= 0:
            self.game_state.game.state_manager.change_state("Menu_State")
            self.game_state.game.state_manager.states["Menu_State"].change_menu("GameOverMenu")

    def check_win(self):
        if not self.game_state.wave_manager.wave_ongoing:
            if self.game_state.wave_manager.wave_number == GAME_DATA[self.game_state.difficulty]["Last Wave"]:
                self.game_state.game.state_manager.change_state("Menu_State")
                self.game_state.game.state_manager.states["Menu_State"].change_menu("WinMenu")

