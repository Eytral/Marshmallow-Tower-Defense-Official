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
            path (list): A list of grid coordinates representing the enemy's path.
        """
        super().__init__(start_position, path, reward=12, health=50, speed=1, sprite=sprites.CRACKER_SPRITE)
        
        # Unimplemented sprite for when the Cracker "breaks":
        self.broken_sprite = sprites.BROKEN_CRACKER_SPRITE  
        self.broken = False  # Indicates whether the Cracker is broken or not
        self.armour = 6  # Initial armor value

    def become_broken(self):
        """
        When the Cracker's health drops below 20%, it moves faster.
        It also "breaks" visually and loses its armor.
        """
        self.speed = 2  # Increase speed after breaking
        self.broken = True  # Mark the Cracker as broken
        self.sprite = self.broken_sprite  # Change sprite to broken one
        self.armour = 0  # Remove armor after breaking

    def take_damage(self, damage, **kwargs):
        """
        Handles taking damage, including immunity to fire damage.
        
        Args:
            damage (int): The amount of damage to be taken.
            **kwargs: Optional keyword arguments, such as damage type.
        
        Special mechanics:
        - Fire damage is ignored (Cracker is immune to fire).
        - Bomb damage triggers the "break" mechanic if Cracker isn't already broken.
        - If health drops below 50%, Cracker will "break" and gain speed.
        """
        print(f"OG cracker damage is: {damage}")
        
        # Armor reduces incoming damage (armor is halved before applying)
        damage -= self.armour // 2
        if damage < 0.5:
            damage = 0.5  # Ensure a minimum damage value

        # Handle different damage types
        if 'damage_type' in kwargs:
            damage_type = kwargs['damage_type']
            
            # Cracker is immune to fire damage, so it's reduced drastically
            if damage_type == "Fire":
                damage /= 10  # Fire damage is negligible
            
            # Bomb damage triggers the "break" mechanic if not already broken
            if damage_type == "Bomb":
                if not self.broken:
                    self.become_broken()

        # If health drops below 50%, trigger the "break" mechanic
        if self.health <= self.max_health // 2 and not self.broken:
            self.become_broken()

        print(f"cracker enemy damage taken is: {damage}")
        
        # Apply the modified damage amount using the parent class method
        super().take_damage(damage)
