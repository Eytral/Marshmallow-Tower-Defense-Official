import pygame
from Constants import config
from Constants import sprites
from Game.Map.grid import Grid
from Game.Map.maps import MAP_DATA
import copy

class Map:
    """
    Represents a game map, managing its grid, background, and music.
    """

    def __init__(self, name):
        """
        Initializes the Map instance.
        
        Args:
            name: The name of the map to load.
        
        Raises:
            ValueError: If the specified map name does not exist in MAP_DATA.
        """
        self.name = name

        if name not in MAP_DATA:
            raise ValueError(f"Map {name} not found")
        
        self.map_grid = Grid(copy.deepcopy(MAP_DATA[name]["grid"]))
        self.background_image = sprites.MARSH_MALLOWS_SPRITE  # Placeholder background
        self.music = MAP_DATA[name]["music"]
        self.enemy_path = self.determine_enemy_path()
        self.enemy_start_pos = self.determine_enemy_start_pos()

    def draw(self, screen, draw_background=False, **kwargs):
        """
        Renders the map background and grid.
        
        Args:
            screen: pygame display surface.
            draw_background: Boolean flag to control background rendering.
        """
        if draw_background:
            screen.blit(self.background_image, (0, config.SCREEN_TOPBAR_HEIGHT))
        else:
            pygame.draw.rect(screen, (200, 200, 200), (0, config.SCREEN_TOPBAR_HEIGHT, config.GRID_SIZE, config.GRID_SIZE)) # Static white colour background
        self.map_grid.draw(screen)

    def preview_tower_placement_square(self, screen, grid_x, grid_y):
        """
        Previews where the player is trying to place a tower on the grid.
        
        Args:
            screen: pygame display surface.
            grid_x: X-coordinate in the grid.
            grid_y: Y-coordinate in the grid.
        """
        result = self.check_tile((grid_x, grid_y))
        if result == "empty space":
            self.map_grid.highlight_square(screen, grid_x, grid_y, (0, 200, 25))  # Green for empty
        else:
            self.map_grid.highlight_square(screen, grid_x, grid_y, (255, 0, 0))  # Red for blocked

    def check_tile(self, grid_coords):
        """
        Checks the type of tile at the given grid coordinates.
        
        Args:
            grid_coords: Tuple (x, y) representing the grid position.
        
        Returns:
            The tile type at the given coordinates.
        """
        return self.map_grid.check_tile(grid_coords)

    def place_tower(self, x, y):
        """
        Attempts to place a tower at the specified grid coordinates.
        
        Args:
            x: X-coordinate of the grid.
            y: Y-coordinate of the grid.
        
        Returns:
            bool: Whether the tower was successfully placed.
        """
        if self.check_tile((x, y)) == "empty space":
            self.map_grid.set_tile(2, x, y)  # Set tower on the grid
            print(f"Successfully placed tower at ({x}, {y})")
            return True
        else:
            print(f"Failed to place tower at ({x}, {y}): Invalid tile")
            return False
        
    def remove_tower(self, x, y):
        """
        Removes a tower from the specified grid coordinates.
        
        Args:
            x: X-coordinate of the grid.
            y: Y-coordinate of the grid.
        
        Returns:
            bool: Whether the tower was successfully removed.
        """
        if self.map_grid.check_tile((x, y)) == "tower":
            self.map_grid.set_tile(0, x, y)  # Reset tile to empty
            print(f"Successfully removed tower at ({x}, {y})")
            return True
        else:
            print(f"Failed to remove tower at ({x}, {y}): No tower found")
            return False

    def determine_enemy_path(self):
        """
        Determines the enemy path based on the grid layout.
        
        Returns:
            list: A list representing the path enemies will follow.
        """
        return self.map_grid.find_path()

    def determine_enemy_start_pos(self):
        """
        Determines the starting position of enemies on the map.
        
        Returns:
            tuple: The starting position coordinates (x, y).
        """
        return self.map_grid.find_enemy_start_pos()

    def reset_map(self):
        """
        Resets the map grid to its default state, removing any placed towers.
        """
        self.map_grid.grid = copy.deepcopy(MAP_DATA[self.name]["grid"])
        print(f"Map {self.name} reset successfully.")
