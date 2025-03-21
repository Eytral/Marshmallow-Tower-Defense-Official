from Constants import sprites
from Entities.Towers.base_tower import Tower

class Turret(Tower):
    """
    A specific tower type that represents a Turret tower. It inherits from the Tower base class
    and has its own unique attributes such as range, fire rate, bullet speed, and bullet damage.
    """

    def __init__(self, x_grid_pos, y_grid_pos):
        """
        Initializes a Turret tower with predefined attributes like range, fire rate, bullet speed,
        bullet damage, and cost. This tower uses a specific sprite for its visual representation.

        Args:
            x_grid_pos: X grid position of the tower on the map.
            y_grid_pos: Y grid position of the tower on the map.
        """
        # Initialize the parent Tower class with the given grid position and specific attributes
        super().__init__(x_grid_pos, y_grid_pos, range=3, fire_rate=30, bullet_speed=15, bullet_damage=3, cost=20)

        # Set the specific sprite for the Turret tower
        self.sprite = sprites.TURRET_TOWER_SPRITE

    def upgrade(self):
        """
        Upgrade logic for the Turret tower.

        This method is currently not implemented, but it is meant to handle upgrading the tower's attributes.
        """
        pass
