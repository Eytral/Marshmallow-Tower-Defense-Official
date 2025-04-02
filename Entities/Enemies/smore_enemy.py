from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class Smore(Enemy):
    """
    Represents a Smore enemy in the game.
    
    S'mores are high-health enemies with a high reward value upon defeat.
    They are relatively slow and have a unique mechanic when they die (splitting into multiple enemies).
    """

    def __init__(self, start_position, path):
        """
        Initializes a Smore enemy with specific attributes.
        
        Args:
            start_position (tuple): The (x, y) starting position of the enemy.
            end_position (tuple): The (x, y) ending position of the enemy.
            path (list): A list of grid coordinates representing the enemy's path.
        """
        # Calls the parent class constructor to set common enemy attributes
        super().__init__(start_position, path, reward=35, health=200, speed=1)

        # Assigns the default sprite for the Smore
        self.sprite = sprites.SMORE_SPRITE

    def die(self, game_state):
        """
        The unique death mechanic for the Smore: when it dies, it splits into multiple smaller enemies.
        (Currently unimplemented)
        """
        super().die(game_state)
        game_state.create_enemy("cracker enemy", Start_Position=self.position, Path=self.path)
        game_state.create_enemy("marshmallow enemy", Start_Position=self.position, Path=self.path)
        game_state.create_enemy("dark_chocolate enemy", Start_Position=self.position, Path=self.path)
        game_state.create_enemy("cracker enemy", Start_Position=self.position, Path=self.path)
        
