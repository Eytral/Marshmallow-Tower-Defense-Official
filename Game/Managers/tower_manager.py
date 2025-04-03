from Entities.Towers.Bird_Flamethrower_tower import BirdFlamethrowerTower
from Entities.Towers.Bomb_tower import BombTower
from Entities.Towers.Laser_tower import LaserTower
from Entities.Towers.Saw_tower import SawTower
from Entities.Towers.Turret_Tower import TurretTower


class TowerManager():
    def __init__(self, game_state):
        self.game_state = game_state
        # Dictionary to store towers (key: grid position, value: tower object)
        self.towers = {}

    def update_towers(self):
        """Update all towers, making them attack enemies if applicable."""
        for _, tower in self.towers.items():
            tower.update(self.game_state.enemy_manager.enemies, self.game_state.bullet_manager.bullets)

    def create_tower(self, tower, position):
        self.towers[(self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y)] = tower(*position)

    def place_tower(self):
        """
        Places a tower on the map grid and adds the selected tower to the game_state tower dict
        """
        print("trying to place tower")
        if self.game_state.money >= self.game_state.mouse.current_selection(0,0).cost:
            if self.game_state.map.place_tower(self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y): # If able to place tower
                self.create_tower(self.game_state.mouse.current_selection, (self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y)) # Create new tower object
                self.game_state.money -= self.game_state.mouse.current_selection(0,0).cost # Removes the cost of the tower from money
                print(f"successfully placed tower, tower list is{self.towers}") # print dictionary of towers for debugging purposes
                self.game_state.mouse.change_current_action(None, None) # Reset mouse action and selection
            else:
                self.game_state.ui_manager.select_tile()
        else:
            if self.game_state.map.check_tile((self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y)) != "outside grid":
                self.game_state.ui_manager.error_message = "Not enough money to place tower"
                self.game_state.mouse.change_current_action(None, None)
            else:
                self.game_state.ui_manager.select_tile()

    def remove_tower(self): # If able to remove tower
        """
        Removes a tower on the map grid and removes the selected tower from the game_state tower dict
        """
        self.game_state.money += self.towers[(self.game_state.mouse.current_selection.x_grid_pos, self.game_state.mouse.current_selection.y_grid_pos)].value//2
        self.game_state.map.remove_tower(self.game_state.mouse.current_selection.x_grid_pos, self.game_state.mouse.current_selection.y_grid_pos)
        del self.towers[(self.game_state.mouse.current_selection.x_grid_pos, self.game_state.mouse.current_selection.y_grid_pos)] # Delete selected tower object (at selected map coordinate)
        print(f"successfully deleted tower, tower list is{self.towers}") # print dictionary of towers for debugging purposes
        self.game_state.mouse.change_current_action(None, None) # Reset mouse action and selection

    def upgrade_tower(self):
        result = self.game_state.mouse.current_selection.upgrade(self.game_state.money)
        if result[0]:
            self.game_state.money -= result[1]
        else:
            self.game_state.ui_manager.error_message = result[1]

    
    def draw_towers(self, screen):
        """Draw all towers on the screen."""
        for _, tower in self.towers.items():
            tower.draw(screen)

    def draw(self, screen):
        self.draw_towers(screen)  # Draw all towers