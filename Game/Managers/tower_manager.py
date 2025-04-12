from Entities.Towers.Bird_Flamethrower_tower import BirdFlamethrowerTower
from Entities.Towers.Bomb_tower import BombTower
from Entities.Towers.Laser_tower import LaserTower
from Entities.Towers.Saw_tower import SawTower
from Entities.Towers.Turret_Tower import TurretTower

class TowerManager:
    """
    Manages towers in the game.
    """
    def __init__(self, game_state):
        """
        Initializes the TowerManager to manage all tower-related operations.

        Args:
            game_state: A reference to the current game state object.
        """
        self.game_state = game_state
        # Dictionary to store towers (key: grid position, value: tower object)
        self.towers = {}

    def update_towers(self):
        """
        Updates all towers, making them attack enemies if applicable.
        This method is called every frame to update the status of each tower.
        """
        for _, tower in self.towers.items():
            tower.update(self.game_state.enemy_manager.enemies, self.game_state.bullet_manager.bullets)

    def create_tower(self, tower, position):
        """
        Creates and adds a tower to the tower dictionary at a specific position.

        Args:
            tower: The class of the tower to be placed (e.g., BirdFlamethrowerTower).
            position: A tuple (x, y) specifying the grid position for the tower.
        """
        self.towers[(self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y)] = tower(*position)

    def place_tower(self):
        """
        Places a tower on the map grid and adds the selected tower to the game_state tower dict.

        Checks if the player has enough money and if the tower placement is valid.
        Displays an error message if the tower cannot be placed.
        """
        print("Trying to place tower")
        # Check if player has enough money to place the selected tower
        if self.game_state.money >= self.game_state.mouse.current_selection(0, 0).cost:
            # Check if the tower can be placed on the grid
            if self.game_state.map.place_tower(self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y):
                # Create the tower and update the player's money
                self.create_tower(self.game_state.mouse.current_selection, (self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y))
                self.game_state.money -= self.game_state.mouse.current_selection(0, 0).cost
                print(f"Successfully placed tower, tower list is {self.towers}")
                self.game_state.mouse.change_current_action(None, None)  # Reset mouse action and selection
            else:
                self.game_state.ui_manager.select_tile()
                if self.game_state.mouse.map_grid_x is not None and self.game_state.mouse.map_grid_y is not None:
                    self.game_state.ui_manager.change_error_message("Invalid Tower Placement")
        else:
            if self.game_state.map.check_tile((self.game_state.mouse.map_grid_x, self.game_state.mouse.map_grid_y)) != "outside grid":
                self.game_state.ui_manager.change_error_message("Not enough money to place tower")
                self.game_state.mouse.change_current_action(None, None)
            else:
                self.game_state.ui_manager.select_tile()

    def remove_tower(self):
        """
        Removes a tower from the map grid and deletes the selected tower from the game_state tower dict.

        Adds half the value of the tower back to the player's money.
        """
        self.game_state.money += self.towers[(self.game_state.mouse.current_selection.x_grid_pos, self.game_state.mouse.current_selection.y_grid_pos)].value // 2
        self.game_state.map.remove_tower(self.game_state.mouse.current_selection.x_grid_pos, self.game_state.mouse.current_selection.y_grid_pos)
        del self.towers[(self.game_state.mouse.current_selection.x_grid_pos, self.game_state.mouse.current_selection.y_grid_pos)]  # Delete selected tower
        print(f"Successfully deleted tower, tower list is {self.towers}")
        self.game_state.mouse.change_current_action(None, None)  # Reset mouse action and selection

    def upgrade_tower(self):
        """
        Upgrades the selected tower if the player has enough money.

        Displays an error message if the upgrade cannot be completed.
        """
        result = self.game_state.mouse.current_selection.upgrade(self.game_state.money)
        print(result)
        if result[0]:
            self.game_state.money -= result[1]  # Deduct cost of upgrade
        else:
            self.game_state.ui_manager.change_error_message(result[1])

    def draw_towers(self, screen):
        """
        Draws all towers on the screen.

        Args:
            screen: The game screen where the towers will be drawn.
        """
        for _, tower in self.towers.items():
            tower.draw(screen)

    def draw(self, screen):
        """
        Draws all towers using the draw_towers method.

        Args:
            screen: The game screen where the towers will be drawn.
        """
        self.draw_towers(screen)  # Draw all towers
