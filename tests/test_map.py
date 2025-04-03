import pytest
from Game.Map.map import Map
from Game.Map.grid import Grid
from Game.Map.maps import MAP_DATA

@pytest.fixture
def test_map():
    """Fixture to create a test map instance"""
    map_name = list(MAP_DATA.keys())[0]  # Use the first available map
    return Map(map_name)

def test_map_initialization_valid(test_map):
    """Test that the map initializes correctly"""
    assert test_map.name in MAP_DATA
    assert isinstance(test_map.map_grid, Grid)

def test_map_initialization_invalid():
    """Test that an invalid map name raises an error"""
    with pytest.raises(ValueError):
        Map("InvalidMapName")

def test_check_tile(test_map):
    """Test check_tile() returns correct values"""
    grid_x, grid_y = 0, 0
    tile_type = test_map.check_tile((grid_x, grid_y))
    assert tile_type in {"path", "tower", "empty space"}

def test_place_tower_success(test_map):
    """Test placing a tower on an empty space"""
    for y, row in enumerate(test_map.map_grid.grid):
        for x, cell in enumerate(row):
            if cell == 0:  # Find an empty space
                placed = test_map.place_tower(x, y)
                assert placed
                assert test_map.check_tile((x, y)) == "tower"
                return  # Stop after the first success

def test_place_tower_fail(test_map):
    """Test that placing a tower on a path fails"""
    for y, row in enumerate(test_map.map_grid.grid):
        for x, cell in enumerate(row):
            if cell == 1:  # Find a path tile
                placed = test_map.place_tower(x, y)
                assert not placed
                assert test_map.check_tile((x, y)) != "tower"
                return

def test_remove_tower_success(test_map):
    """Test removing a tower"""
    for y, row in enumerate(test_map.map_grid.grid):
        for x, cell in enumerate(row):
            if cell == 0:  # Find an empty space
                test_map.place_tower(x, y)  # Place a tower first
                removed = test_map.remove_tower(x, y)
                assert removed
                assert test_map.check_tile((x, y)) == "empty space"
                return

def test_remove_tower_fail(test_map):
    """Test that removing a tower where none exists fails"""
    for y, row in enumerate(test_map.map_grid.grid):
        for x, cell in enumerate(row):
            if cell == 0:  # Find an empty space
                removed = test_map.remove_tower(x, y)  # No tower placed
                assert not removed
                return

def test_reset_map(test_map):
    """Test that reset_map() restores the original grid"""
    # Modify the map by placing a tower
    for y, row in enumerate(test_map.map_grid.grid):
        for x, cell in enumerate(row):
            if cell == 0:  # Find an empty space
                test_map.place_tower(x, y)
                assert test_map.check_tile((x, y)) == "tower"
                test_map.reset_map()
                assert test_map.check_tile((x, y)) == "empty space"
                return
