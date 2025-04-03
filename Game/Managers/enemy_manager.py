from Game.Core.game_data import ENEMY_CLASS_MAP

class EnemyManager():
    def __init__(self, game_state):
        self.game_state = game_state
        # List to store active enemies
        self.enemies = [] 

    def update_enemies(self):
        """Update each enemy's movement and remove dead or finished enemies."""
        for enemy in self.enemies:
            enemy.update(self.game_state)

    def create_enemy(self, enemy_name, **kwargs):
        if kwargs:
            start_position = kwargs["Start_Position"]
            enemy_path = kwargs["Path"]
        else:
            start_position = self.game_state.map.enemy_start_pos
            enemy_path = self.game_state.map.enemy_path
        print(f"created enemy {enemy_name}")
        enemy_class = ENEMY_CLASS_MAP.get(enemy_name)
        if enemy_class:
            self.enemies.append(enemy_class(start_position, enemy_path))
    

    def draw_enemies(self, screen):
        """Draw all enemies on the screen."""
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def draw(self, screen):
        self.draw_enemies(screen) # Draws all enemies