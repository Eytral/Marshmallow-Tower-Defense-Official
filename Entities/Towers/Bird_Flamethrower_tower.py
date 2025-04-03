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
        upgrade_data = {
            "UPGRADE 1": {
                "Range": 3,
                "Fire Rate": 13,
                "Bullet Speed": 14,
                "Bullet Damage": 7,
                "Cost": 100,
                "Splash Radius": 0
            },

            "UPGRADE 2": {
                "Range": 4,
                "Fire Rate": 10,
                "Bullet Speed": 18,
                "Bullet Damage": 10,
                "Cost": 150,
                "Splash Radius": 0
            },

            "UPGRADE 3": {
                "Range": 5,
                "Fire Rate": 6,
                "Bullet Speed": 20,
                "Bullet Damage": 15,
                "Cost": 250,
                "Splash Radius": 0.5
            }
        }
        super().__init__(x_grid_pos, y_grid_pos, upgrade_data=upgrade_data, range=3, fire_rate=15, bullet_speed=10, bullet_damage=5, cost=45)
        
        # Set the specific sprite for the BirdFlamethrower tower
        self.sprite = sprites.BIRDFLAMETHROWER_TOWER_SPRITE
        

    def shoot(self, bullets):
        """
        Fires a bullet towards the target.
        """
        # Create a bullet and add it to the list of bullets
        bullets.append(Bullet(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage, bullet_type="Fire", tile_splash_radius=self.tile_splash_radius, bullet_sprite=sprites.FIREBALL_SPRITE))

        # Reset the cooldown to the fire rate
        self.shoot_cooldown = self.fire_rate

