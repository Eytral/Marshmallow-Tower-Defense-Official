from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class Marshmallow(Enemy):
    """
    Represents a Marshmallow enemy in the game.
    
    Marshmallows are basic enemies with low health and moderate speed.
    They have a relatively low reward value upon being defeated.
    """

    def __init__(self, start_position, path):
        """
        Initializes a Marshmallow enemy with specific attributes.
        
        Args:
            start_position (tuple): The (x, y) starting position of the enemy.
            end_position (tuple): The (x, y) ending position of the enemy.
            path (list): A list of grid coordinates representing the enemy's path.
        """
        # Calls the parent class constructor to set common enemy attributes
        super().__init__(start_position, path, reward=6, health=20, speed=2)

        # Assigns the default sprite for the Marshmallow
        self.sprite = sprites.MARSHMALLOW_SPRITE
