import pytest
import pygame
from Constants import config, sprites
from Entities.Enemies.base_enemy import Enemy

# Mocking necessary imports for sprites and pygame
@pytest.fixture
def mock_sprites():
    sprites.ENEMY_DEFAULT_SPRITE = pygame.Surface((config.GRID_CELL_SIZE, config.GRID_CELL_SIZE))
    return sprites

@pytest.fixture
def test_enemy(mock_sprites):
    start_position = (0, 0)
    end_position = (5, 5)
    path = []  # Empty path, just for initialization
    return Enemy(start_position, end_position, path)

def test_enemy_initialization(test_enemy):
    """Test initialization of the enemy."""
    assert test_enemy.reward == 5
    assert test_enemy.max_health == 10
    assert test_enemy.health == 10
    assert test_enemy.speed == 2
    assert test_enemy.position == [0, config.SCREEN_TOPBAR_HEIGHT]
    assert test_enemy.grid_position == (0, 0)
    assert test_enemy.end_position == [5 * config.GRID_CELL_SIZE, 5 * config.GRID_CELL_SIZE + config.SCREEN_TOPBAR_HEIGHT]
    assert test_enemy.is_dead == False
    assert test_enemy.reached_end == False

def test_enemy_move(test_enemy):
    """Test that the enemy moves correctly based on its speed."""
    initial_position = test_enemy.position[1]
    
    # Move the enemy once
    test_enemy.move()
    
    # Check if the position has been updated based on the speed
    assert test_enemy.position[1] == initial_position + test_enemy.speed
    assert test_enemy.grid_position == (test_enemy.position[0] // config.GRID_CELL_SIZE, test_enemy.position[1] // config.GRID_CELL_SIZE)

def test_enemy_take_damage(test_enemy):
    """Test that the enemy takes damage correctly."""
    initial_health = test_enemy.health
    
    # Take damage
    test_enemy.take_damage(3)
    
    # Check if health decreased
    assert test_enemy.health == initial_health - 3

def test_enemy_death_check(test_enemy):
    """Test if the enemy dies when health <= 0."""
    test_enemy.take_damage(10)  # Health will be reduced to 0
    
    # Check if the enemy dies
    test_enemy.check_is_dead()
    
    assert test_enemy.is_dead == True
    assert test_enemy.health == 0

def test_enemy_reach_end(test_enemy):
    """Test if the enemy reaches the end position."""
    test_enemy.position = test_enemy.end_position  # Set the enemy's position to the end
    
    # Check if the enemy has reached the end
    test_enemy.check_has_reached_end()
    
    assert test_enemy.reached_end == True

def test_enemy_update(test_enemy):
    """Test the update method (combines movement and death check)."""
    initial_health = test_enemy.health
    initial_position = test_enemy.position[1]
    
    # Update the enemy (move and check death)
    test_enemy.update()
    
    # Check if the enemy has moved
    assert test_enemy.position[1] == initial_position + test_enemy.speed
    
    # Ensure health didn't change if the enemy isn't dead
    assert test_enemy.health == initial_health
