from Constants import sprites
from Entities.Towers.base_tower import Tower
from Entities.bullet import Bullet

class Bomb(Tower):
    """
    A specific tower type that represents a Bomb tower. It inherits from the Tower base class
    and has its own unique attributes, such as range, fire rate, bullet speed, and bullet damage.
    """

    def __init__(self, x_grid_pos, y_grid_pos):
        """
        Initializes a Bomb tower with predefined attributes like range, fire rate, bullet speed,
        bullet damage, and cost. This tower uses a specific sprite for its visual representation.

        Args:
            x_grid_pos: X grid position of the tower on the map.
            y_grid_pos: Y grid position of the tower on the map.
        """
        # Initialize the parent Tower class with the given grid position and specific attributes
        upgrade_data = {
            "UPGRADE 1": {
                "Range": 5,
                "Fire Rate": 60,
                "Bullet Speed": 6,
                "Bullet Damage": 15,
                "Cost": 100,
                "Splash Radius": 1
            },

            "UPGRADE 2": {
                "Range": 6,
                "Fire Rate": 50,
                "Bullet Speed": 7,
                "Bullet Damage": 20,
                "Cost": 150,
                "Splash Radius": 2
            },

            "UPGRADE 3": {
                "Range": 7,
                "Fire Rate": 40,
                "Bullet Speed": 9,
                "Bullet Damage": 30,
                "Cost": 250,
                "Splash Radius": 3
            }
            }

        super().__init__(x_grid_pos, y_grid_pos, upgrade_data=upgrade_data, range=3, tile_splash_radius= 1, fire_rate=75, bullet_speed=6, bullet_damage=11, cost=50)

        # Set the specific sprite for the Bomb tower
        self.sprite = sprites.BOMB_TOWER_SPRITE

    def shoot(self, bullets):
        """
        Fires a bullet towards the target.
        """
        # Create a bullet and add it to the list of bullets
        bullets.append(Bullet(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage, bullet_type="Bomb", tile_splash_radius=self.tile_splash_radius, bullet_sprite=sprites.BOMB_SPRITE))

        # Reset the cooldown to the fire rate
        self.shoot_cooldown = self.fire_rate