from Constants import sprites
from Entities.Towers.base_tower import Tower
from Entities.Projectiles.flame import Flame

class BirdFlamethrowerTower(Tower):
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
        tower_data = {

            "UPGRADE 0": {
                "Range": 3,
                "Attack delay": 15,
                "Bullet Speed": 10,
                "Bullet Damage": 5,
                "Cost": 45,
            },

            "UPGRADE 1": {
                "Range": 3,
                "Attack delay": 13,
                "Bullet Speed": 14,
                "Bullet Damage": 7,
                "Cost": 100,
            },

            "UPGRADE 2": {
                "Range": 4,
                "Attack delay": 10,
                "Bullet Speed": 18,
                "Bullet Damage": 10,
                "Cost": 150,
            },

            "UPGRADE 3": {
                "Range": 5,
                "Attack delay": 6,
                "Bullet Speed": 20,
                "Bullet Damage": 15,
                "Cost": 250,
            }
        }
        super().__init__(x_grid_pos, y_grid_pos, tower_data=tower_data, range=3, attack_delay=15, bullet_speed=10, bullet_damage=5, cost=45)
        
        # Set the specific sprite for the BirdFlamethrower tower
        self.sprite = sprites.BIRDFLAMETHROWER_TOWER_SPRITE
        

    def shoot(self, bullets):
        """
        Fires a bullet towards the target.
        """
        # Create a bullet and add it to the list of bullets
        bullets.append(Flame(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage, bullet_type="Fire", bullet_sprite=sprites.FIREBALL_SPRITE))

        # Reset the cooldown to the fire rate
        self.shoot_cooldown = self.attack_delay

