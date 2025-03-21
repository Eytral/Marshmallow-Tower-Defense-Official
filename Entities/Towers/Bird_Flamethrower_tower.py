from Constants import sprites
from Entities.Towers.base_tower import Tower

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
        super().__init__(x_grid_pos, y_grid_pos, range=1, fire_rate=20, bullet_speed=20, bullet_damage=2, cost=30)
        
        # Set the specific sprite for the BirdFlamethrower tower
        self.sprite = sprites.BIRDFLAMETHROWER_TOWER_SPRITE
    
    def upgrade(self):
        """
        Upgrade logic for the BirdFlamethrower tower.
        
        This method is currently not implemented, but it is meant to handle upgrading the tower's attributes.
        """
        pass
