from Entities.Enemies.base_enemy import Enemy
from Constants import sprites, config

class Cracker(Enemy):
    """
    Represents a Cracker enemy in the game.
    
    The Cracker starts with a set amount of health and speed.
    It has a unique mechanic where, when its health drops below 20%,
    it moves faster. Additionally, it is immune to fire damage.
    """

    def __init__(self, start_position, path):
        """
        Initializes a Cracker enemy with specific attributes.
        
        Args:
            start_position (tuple): The (x, y) starting position of the enemy.
            end_position (tuple): The (x, y) ending position of the enemy.
            path (list): A list of grid coordinates representing the enemy's path.
        """
        super().__init__(start_position, path, reward=12, health=70, speed=1)
        
        # Assigns the default sprite for the Cracker
        self.sprite = sprites.CRACKER_SPRITE
        
        # Unimplemented sprite for when cracker "breaks":
        self.broken_sprite = sprites.BROKEN_CRACKER_SPRITE  
        self.broken = False

    def become_broken(self):
        """
        When the Cracker's health drops below 20%, it moves faster.
        """
        # 20% of original health
        self.speed = 2  # Increase speed after breaking
        self.broken = True
        self.sprite = self.broken_sprite  

    def take_damage(self, damage, **kwargs):
        """
        Handles taking damage, including immunity to fire damage.
        
        Args:
            damage (int): The amount of damage to be taken.
            **kwargs: Optional keyword arguments, such as damage type.
        
        Fire damage is ignored (Cracker is immune to fire).
        """
        if 'damage_type' in kwargs:
            damage_type = kwargs['damage_type']
            if damage_type == "Fire":
                damage = 0  # Negate fire damage
            if damage_type == "Bomb":
                if not self.broken:
                    self.become_broken()
        if self.health <= self.max_health // 2:  # 50% of original health
            if not self.broken:
                self.become_broken()
        if self.broken:
            damage *= 2
        
        # Apply the modified damage amount using the parent class method
        super().take_damage(damage)
