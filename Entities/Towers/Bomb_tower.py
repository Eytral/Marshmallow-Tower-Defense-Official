from Constants import sprites
from Entities.Towers.base_tower import Tower

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
        super().__init__(x_grid_pos, y_grid_pos, range=3, fire_rate=50, bullet_speed=5, bullet_damage=10, cost=50)

        # Set the specific sprite for the Bomb tower
        self.sprite = sprites.BOMB_TOWER_SPRITE

    def upgrade(self):
        """
        Upgrade logic for the Bomb tower.

        This method is currently not implemented, but it is meant to handle upgrading the tower's attributes.
        """
        pass
