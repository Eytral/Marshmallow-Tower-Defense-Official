from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class WhiteChocolate(Enemy):
    """
    Represents a White Chocolate enemy in the game.
    
    White Chocolate is a fast enemy that has a special vulnerability to fire. 
    When exposed to fire damage, it melts, losing its speed and changing its appearance.
    """

    def __init__(self, start_position, path):
        """
        Initializes a White Chocolate enemy with specific attributes.
        
        Args:
            start_position (tuple): The (x, y) starting position of the enemy.
            path (list): A list of grid coordinates representing the enemy's path.
        """
        # Calls the parent class constructor to set common enemy attributes
        super().__init__(start_position, path, reward=20, health=40, speed=5, sprite=sprites.WHITE_CHOCOLATE_SPRITE)

        # White Chocolate’s appearance after melting
        self.melted_sprite = sprites.MELTED_WHITE_CHOCOLATE_SPRITE  

    def take_damage(self, damage, **kwargs):
        """
        Handles damage taken, factoring in vulnerability to fire.
        
        Args:
            damage (int): The amount of damage to be taken.
            **kwargs: Optional keyword arguments, such as damage type.

        Special mechanic:
        - If hit by fire damage, White Chocolate melts, reducing its speed.
        """
        if 'damage_type' in kwargs:
            damage_type = kwargs['damage_type']
            
            # Fire damage melts White Chocolate, slowing it down
            if damage_type == "Fire":
                self.melt()
        
        # Apply the damage using the parent class method
        super().take_damage(damage)

    def melt(self):
        """
        When White Chocolate melts:
        - Its speed is reduced.
        - Its sprite changes to a melted appearance.
        """
        self.speed = 2  # Reduce speed after melting
        
        # Change to melted sprite
        self.sprite = self.melted_sprite
