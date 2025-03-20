import pygame
from Constants import config

class Grid:
    """
    Represents a grid structure that stores map data and handles rendering.
    """
    
    def __init__(self, grid):
        """
        Initializes the Grid instance.
        
        Args:
            grid: A 2D list representing the grid structure.
        """
        self.grid = grid

    def check_tile(self, grid_coords):
        """
        Determines the type of tile at the given grid coordinates.
        
        Args:
            grid_coords: Tuple (x, y) representing the grid position.
        
        Returns:
            A string indicating the tile type ("path", "tower", or "empty space").
        """
        grid_x, grid_y = grid_coords[0], grid_coords[1]
        if grid_x is not None and grid_y is not None:
            if self.grid[grid_y][grid_x] == 1 or self.grid[grid_y][grid_x] == 3:
                return "path"
            elif self.grid[grid_y][grid_x] == 2:
                return "tower"
            else:
                return "empty space"

    def set_tile(self, tile, grid_x, grid_y):
        """
        Sets the specified tile type at the given grid coordinates.
        
        Args:
            tile: The tile type to place.
            grid_x: X-coordinate of the grid.
            grid_y: Y-coordinate of the grid.
        """
        self.grid[grid_y][grid_x] = tile
    

    def draw(self, screen):
        """
        Renders the grid and highlights the selected cell.
        
        Args:
            screen: pygame display surface.
            grid_x: X-coordinate of the highlighted grid cell.
            grid_y: Y-coordinate of the highlighted grid cell.
        """
        self.draw_grid(screen)

    def draw_grid(self, screen):
        """
        Draws the grid lines and visualizes tile types.
        
        Args:
            screen: pygame display surface.
        """
        for x in range(0, config.GRID_SIZE, config.GRID_CELL_SIZE):
            for y in range(config.SCREEN_TOPBAR_HEIGHT, config.GRID_SIZE + config.SCREEN_TOPBAR_HEIGHT, config.GRID_CELL_SIZE):
                pygame.draw.rect(screen, (200, 200, 200), (x, y, config.GRID_CELL_SIZE, config.GRID_CELL_SIZE), 1)

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * config.GRID_CELL_SIZE + config.OFFSET_FROM_GRID, y * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT + config.OFFSET_FROM_GRID, config.GRID_CELL_SIZE-config.OFFSET_FROM_GRID*2, config.GRID_CELL_SIZE-config.OFFSET_FROM_GRID*2)
                if cell == 1:
                    pygame.draw.rect(screen, (255, 165, 0), rect)  # Draw orange for path tiles
                if cell == 3:
                    pygame.draw.rect(screen, (255, 0, 0), rect)  # Draw red for starting point tile

        border_rect = pygame.Rect(0, config.SCREEN_TOPBAR_HEIGHT, config.GRID_SIZE, config.GRID_SIZE)
        pygame.draw.rect(screen, (0, 0, 255), border_rect, 1)  # Draw a border (thickness = 1)
