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
        super().__init__(x_grid_pos, y_grid_pos, range=5, fire_rate=75, bullet_speed=6, bullet_damage=10, cost=50)

        # Set the specific sprite for the Bomb tower
        self.sprite = sprites.BOMB_TOWER_SPRITE

    def shoot(self):
        """
        Fires a bullet towards the target.
        """
        # Create a bullet and add it to the list of bullets
        self.bullets.append(Bullet(self.x_centre_pos, self.y_centre_pos, self.target, self.bullet_speed, self.bullet_damage, bullet_type="Bomb", bullet_sprite=sprites.BOMB_SPRITE))

        # Reset the cooldown to the fire rate
        self.shoot_cooldown = self.fire_rate

    def upgrade(self):
        """
        Upgrade logic for the Bomb tower.

        This method is currently not implemented, but it is meant to handle upgrading the tower's attributes.
        """
        pass
