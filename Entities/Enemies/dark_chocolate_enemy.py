from Entities.Enemies.base_enemy import Enemy
from Constants import sprites

class DarkChocolate(Enemy):
    """
    Represents a Dark Chocolate enemy in the game.
    
    Dark Chocolate is fast but has armor that reduces incoming damage.
    However, it is vulnerable to fire, which removes its armor and slows it down.
    """

    def __init__(self, start_position, path):
        """
        Initializes a Dark Chocolate enemy with specific attributes.
        
        Args:
            start_position (tuple): The (x, y) starting position of the enemy.
            path (list): A list of grid coordinates representing the enemy's path.
        """
        super().__init__(start_position, path, reward=18, health=50, speed=3, sprite=sprites.DARK_CHOCOLATE_SPRITE)
        
        self.melted_sprite = sprites.MELTED_DARK_CHOCOLATE_SPRITE  # Sprite when melted

        # Armor reduces incoming damage (damage is divided by armor value)
        self.armour = 3  # Initial armor value

    def take_damage(self, damage, **kwargs):
        """
        Handles damage taken, factoring in armor reduction.
        
        Args:
            damage (int): The amount of damage to be taken.
            **kwargs: Optional keyword arguments, such as damage type.

        Special mechanics:
        - If hit by fire damage, Dark Chocolate melts, losing its armor and slowing down.
        - If it has armor, the damage is reduced before being applied.
        """
        if 'damage_type' in kwargs:
            damage_type = kwargs['damage_type']
            
            # Fire damage melts Dark Chocolate, removing armor and slowing it down
            if damage_type == "Fire":
                self.melt()
        
        # Reduce damage if armor is still active
        if self.armour != 0:
            damage -= self.armour  # Armor acts as a damage reduction
            if damage < 0.5:  # Ensure a minimum damage of 0.5 to avoid infinite durability
                damage = 0.5
        
        # Apply the modified damage amount using the parent class method
        super().take_damage(damage)

    def melt(self):
        """
        When Dark Chocolate melts:
        - Its speed is reduced, making it slower.
        - It loses all armor, making it vulnerable to future attacks.
        - (Optional) Sprite changes to a melted appearance.
        """
        self.speed = 2  # Reduce speed after melting
        self.armour = 0  # Remove armor protection

        self.sprite = self.melted_sprite  # Change to melted appearance
