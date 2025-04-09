import pygame
from Constants import config

class Grid:
    """
    Represents a grid structure that stores map data and handles rendering.
    The grid is used to manage tiles, check for types, and draw the grid on the screen.
    """
    
    def __init__(self, grid):
        """
        Initializes the Grid instance.
        
        Args:
            grid: A 2D list representing the grid structure. Each cell in the list
                  corresponds to a tile in the grid.
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
        
        # Check if the coordinates are within the bounds of the grid
        if grid_x is not None and grid_y is not None:
            if grid_y >= len(self.grid) or grid_y < 0 or grid_x >= len(self.grid[0]) or grid_x < 0:
                raise IndexError  # Raise an exception if coordinates are out of bounds
        
        # Return tile type based on the value at the coordinates
            if self.grid[grid_y][grid_x] == 1 or self.grid[grid_y][grid_x] == 3 or self.grid[grid_y][grid_x] == 4:
                return "path"  # A path tile
            elif self.grid[grid_y][grid_x] == 2:
                return "tower"  # A tower tile
            else:
                return "empty space"  # An empty space tile
        else:
            return "outside grid"

    def set_tile(self, tile, grid_x, grid_y):
        """
        Sets the specified tile type at the given grid coordinates.
        
        Args:
            tile: The tile type to place (e.g., 1 for path, 2 for tower).
            grid_x: X-coordinate of the grid.
            grid_y: Y-coordinate of the grid.
        """
        # Check if the coordinates are within bounds
        if grid_y >= len(self.grid) or grid_y < 0 or grid_x >= len(self.grid[0]) or grid_x < 0:
            raise IndexError  # Raise an exception if coordinates are out of bounds
        
        # Set the tile type at the specified grid coordinates
        self.grid[grid_y][grid_x] = tile

    def draw(self, screen):
        """
        Renders the grid and highlights the selected cell (if any).
        
        Args:
            screen: pygame display surface where the grid will be drawn.
        """
        # Call the function to draw the grid
        self.draw_grid(screen)

    def draw_grid(self, screen):
        """
        Draws the grid lines and visualizes tile types (path, tower, empty).
        
        Args:
            screen: pygame display surface where the grid and tiles will be drawn.
        """
        # Loop through grid cells to draw grid lines
        for x in range(0, config.GRID_SIZE, config.GRID_CELL_SIZE):
            for y in range(config.SCREEN_TOPBAR_HEIGHT, config.GRID_SIZE + config.SCREEN_TOPBAR_HEIGHT, config.GRID_CELL_SIZE):
                # Draw grid lines with light gray color
                pygame.draw.rect(screen, (200, 200, 200), (x, y, config.GRID_CELL_SIZE, config.GRID_CELL_SIZE), 1)

        # Loop through each row and column of the grid to draw the tiles
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                # Define the rectangle for each tile, factoring in the grid offset
                rect = pygame.Rect(x * config.GRID_CELL_SIZE + config.OFFSET_FROM_GRID, 
                                   y * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT + config.OFFSET_FROM_GRID, 
                                   config.GRID_CELL_SIZE - config.OFFSET_FROM_GRID * 2, 
                                   config.GRID_CELL_SIZE - config.OFFSET_FROM_GRID * 2)
                
                # Draw tiles based on their type using color codes
                if cell == 0 or cell == 2:
                    pygame.draw.rect(screen, (0, 100, 0), rect)  # Dark Green for empty/tower tiles
                if cell == 1:
                    pygame.draw.rect(screen, (200, 140, 0), rect)  # Orange for path tiles
                if cell == 3:
                    pygame.draw.rect(screen, (0, 200, 0), rect)  # Green for starting point tiles
                if cell == 4:
                    pygame.draw.rect(screen, (200, 0, 0), rect)  # Red for ending point tiles

        # Draw a border around the entire grid
        border_rect = pygame.Rect(0, config.SCREEN_TOPBAR_HEIGHT, config.GRID_SIZE, config.GRID_SIZE)
        pygame.draw.rect(screen, (0, 0, 255), border_rect, 1)  # Blue border with thickness of 1

    def highlight_square(self, screen, grid_x, grid_y, colour=(255, 0, 0)):
        """
        Highlights the selected grid square.
        
        Args:
            screen: pygame display surface.
            grid_x: X-coordinate of the grid cell.
            grid_y: Y-coordinate of the grid cell.
        """
        if grid_x is not None and grid_y is not None:
            pygame.draw.rect(screen, colour, (grid_x * config.GRID_CELL_SIZE, grid_y * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT, config.GRID_CELL_SIZE, config.GRID_CELL_SIZE), 3)  # Red highlight
        else:
            raise TypeError


    def find_path(self):
    # Find the start position (3)
        start = None
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == 3:  # Look for the start marker
                    start = (r, c)
                    break
            if start:
                break

        if not start:
            print("Start position (3) not found in the grid.")
            return []  # Return an empty list if start not found

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Movement directions

        path = [start]
        visited = set([start])
        current_position = start

        while True:
            found_next_step = False
            possible_moves = []

            # Check all possible directions
            for dr, dc in directions:
                nr, nc = current_position[0] + dr, current_position[1] + dc

                # Ensure we stay within bounds, check for valid path (1), and avoid revisiting cells
                if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                    if self.grid[nr][nc] == 1 and (nr, nc) not in visited:
                        possible_moves.append((nr, nc))

            if not possible_moves:
                print(f"Dead end reached at {current_position}, breaking out.")
                break  # No valid path found, exit loop

            next_position = possible_moves[0]  # Pick the first valid move

            # Add the next position to the path and mark it as visited
            visited.add(next_position)
            path.append(next_position)
            current_position = next_position

            print(f"Moving from {current_position} to {next_position}")

        print(f"Enemy grid path: {path}")
        # Convert the path coordinates into screen positions
        path_positions = []
        for coordinate in path:
            x, y = (coordinate[1]) * config.GRID_CELL_SIZE, coordinate[0] * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT
            path_positions.append((x, y))

        print(f"Enemy path (screen positions): {path_positions}")

        return path_positions
        
    def find_enemy_start_pos(self):
        for row_num, row in enumerate(self.grid):
            for column_num, space in enumerate(row):
                if space == 3:
                    x, y = column_num*config.GRID_CELL_SIZE, row_num*config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT 
                    return (x, y)
        return (0,0)