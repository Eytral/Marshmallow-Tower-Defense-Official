import pygame
from Constants import config
from Constants import sprites
from Game.grid import Grid
from Game.maps import MAP_DATA
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
        self.background_image = sprites.MARSH_MALLOWS_SPRITE
        self.music = MAP_DATA[name]["music"]

    def draw(self, screen, grid_x, grid_y):
        """
        Renders the map background and grid.
        
        Args:
            screen: pygame display surface.
        """
        screen.blit(self.background_image, (0, config.SCREEN_TOPBAR_HEIGHT))
        self.map_grid.draw(screen, grid_x, grid_y)

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
        """
        if self.check_tile((x,y)) == "empty space":
            self.map_grid.set_tile(2, x, y)
            print("succesfully placed tower")
            return True
        else:
            return False
        
    def remove_tower(self, x, y):
        """
        Removes a tower from the specified grid coordinates.
        
        Args:
            x: X-coordinate of the grid.
            y: Y-coordinate of the grid.
        """
        if self.map_grid.check_tile((x,y)) == "tower":
            self.map_grid.set_tile(0, x, y)
            return True
        else:
            return False

    def determine_enemy_path(self):
        return self.map_grid.find_path()
        
    def determine_enemy_start_pos(self):
        return self.map_grid.find_enemy_start_pos()

    def reset_map(self):
        """
        Resets the map grid to its default state, removing any placed towers.
        """
        self.map_grid.grid = copy.deepcopy(MAP_DATA[self.name]["grid"])
