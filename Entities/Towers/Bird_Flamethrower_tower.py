from Constants import sprites
from Entities.Towers.base_tower import Tower
from Entities.bullet import Bullet

class BirdFlamethrower(Tower):
    """
    A specific tower type that represents a Bird Flamethrower tower. It inherits from the Tower base class 
    and has its own unique attributes, such as range, fire rate, bullet speed, and bullet damage.
    """
    
    def __init__(self, x_grid_pos, y_grid_pos):
        """
        Initializes a BirdFlamethrower tower with predefined attributes like range, fire rate, bullet speed, 
        and bullet damage. This tower is specialized and will use a specific sprite.

        Args:
            x_grid_pos: X grid position of the tower on the map.
            y_grid_pos: Y grid position of the tower on the map.
        """
        # Initialize the parent Tower class with the given grid position and specific attributes
        super().__init__(x_grid_pos, y_grid_pos, range=3, fire_rate=8, bullet_speed=18, bullet_damage=5, cost=45)
        
        # Set the specific sprite for the BirdFlamethrower tower
        self.sprite = sprites.BIRDFLAMETHROWER_TOWER_SPRITE

    def shoot(self):
        """
        Fires a bullet towards the target.
        """
        # Create a bullet and add it to the list of bullets
        self.bullets.append(Bullet(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage, bullet_type="Fire", bullet_sprite=sprites.FIREBALL_SPRITE))

        # Reset the cooldown to the fire rate
        self.shoot_cooldown = self.fire_rate


    def upgrade(self):
        """
        Upgrade logic for the BirdFlamethrower tower.
        """
        {
        "UPGRADE 1": {
            "Range": 3,
            "Fire Rate": 7,
            "Bullet Speed": 18,
            "Bullet Damage": 5,
            "Cost": 100
        },

        "UPGRADE 2": {
            "Range": 4,
            "Fire Rate": 6,
            "Bullet Speed": 18,
            "Bullet Damage": 10,
            "Cost": 150
        },

        "UPGRADE 3": {
            "Range": 5,
            "Fire Rate": 5,
            "Bullet Speed": 18,
            "Bullet Damage": 15,
            "Cost": 250
        }
        }
