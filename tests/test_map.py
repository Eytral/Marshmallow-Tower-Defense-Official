import pytest
from Game.Map.map import Map
from Game.Map.maps import MAP_DATA
from Game.Map.grid import Grid
import copy

@pytest.fixture
def test_map():
    """Fixture to create a test map instance"""
    map_name = list(MAP_DATA.keys())[0]  # Use the first available map
    return Map(map_name)

def test_map_initialization_valid(test_map):
    """Test that the map initializes correctly"""
    assert test_map.name in MAP_DATA
    assert isinstance(test_map.map_grid, Grid)
    assert isinstance(test_map.map_grid.grid, list)

def test_map_initialization_invalid():
    """Test that an invalid map name raises an error"""
    with pytest.raises(ValueError):
        Map("InvalidMapName")

def test_check_tile(test_map):
    """Test check_tile() returns correct values"""
    x, y = 0, 0
    tile_type = test_map.check_tile((x, y))
    assert tile_type in {"path", "tower", "empty space"}

def test_place_tower_success(test_map):
    """Test placing a tower on an empty space"""
    for y, row in enumerate(test_map.map_grid.grid):
        for x, cell in enumerate(row):
            if cell == 0:  # Empty space
                assert test_map.place_tower(x, y) is True
                assert test_map.map_grid.grid[y][x] == 2  # Tower placed (represented by 2 in Grid)
                assert test_map.check_tile((x, y)) == "tower"
                return

def test_place_tower_fail(test_map):
    """Test placing a tower on a non-empty space (like a path) fails"""
    for y, row in enumerate(test_map.map_grid.grid):
        for x, cell in enumerate(row):
            if cell == 1:  # Path tile (represented by 1 in Grid)
                assert test_map.place_tower(x, y) is False
                assert test_map.check_tile((x, y)) == "path"
                return

def test_remove_tower_success(test_map):
    """Test removing a tower that was placed"""
    for y, row in enumerate(test_map.map_grid.grid):
        for x, cell in enumerate(row):
            if cell == 0:  # Empty space
                test_map.place_tower(x, y)
                assert test_map.map_grid.grid[y][x] == 2  # Tower placed (represented by 2 in Grid)
                assert test_map.remove_tower(x, y) is True
                assert test_map.map_grid.grid[y][x] == 0  # Empty again (represented by 0 in Grid)
                assert test_map.check_tile((x, y)) == "empty space"
                return

def test_remove_tower_fail(test_map):
    """Test removing a tower from a tile without a tower"""
    for y, row in enumerate(test_map.map_grid.grid):
        for x, cell in enumerate(row):
            if cell == 0:  # Empty space, no tower yet
                assert test_map.remove_tower(x, y) is False
                return

def test_reset_map(test_map):
    """Test that reset_map() restores the original grid"""
    original_grid = copy.deepcopy(test_map.map_grid.grid)  # Store the original grid state
    
    # Place a tower on the first available empty space
    for y, row in enumerate(test_map.map_grid.grid):
        for x, cell in enumerate(row):
            if cell == 0:  # Find an empty space
                test_map.place_tower(x, y)  # Place a tower
                assert test_map.map_grid.grid[y][x] == 2  # Check that a tower is placed (represented by 2 in Grid)
                break
    
    # After placing a tower, the grid should no longer be the same
    assert test_map.map_grid.grid != original_grid
    
    # Call reset_map and verify the grid is restored to its original state
    test_map.reset_map()
    assert test_map.map_grid.grid == original_grid  # Grid should be reset to original
