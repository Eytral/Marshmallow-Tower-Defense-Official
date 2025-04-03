import pytest
from Constants import config, sprites
from Entities.Towers.Bird_Flamethrower_tower import BirdFlamethrower
from Entities.Projectiles.base_projectile import Bullet
from Entities.Enemies.base_enemy import Enemy  # Assuming you have an Enemy class to use

# Use a simple mock for the sprite
@pytest.fixture
def mock_sprites():
    # Mock sprite by setting a simple object (could be a string for this test)
    sprites.TOWER_DEFAULT_SPRITE = "mock_sprite"
    return sprites


@pytest.fixture
def test_tower(mock_sprites):
    """Create a test tower instance."""
    return BirdFlamethrower(x_grid_pos=3, y_grid_pos=3)


@pytest.fixture
def test_enemy():
    """Create a simple enemy instance."""
    enemy = Enemy(start_position=(4, 4), end_position=(5, 5), path=[])
    enemy.is_dead = False
    enemy.reached_end = False
    return enemy


def test_tower_initialization(test_tower):
    """Test initialization of the tower."""
    assert test_tower.x_grid_pos == 3
    assert test_tower.y_grid_pos == 3
    assert test_tower.range == 1
    assert test_tower.fire_rate == 20
    assert test_tower.bullet_speed == 20
    assert test_tower.bullet_damage == 2
    assert test_tower.cost == 30
    assert test_tower.shoot_cooldown == 0
    assert test_tower.target is None
    assert test_tower.bullets == []


def test_tower_in_range(test_tower, test_enemy):
    """Test if an enemy is within the tower's attack range."""
    # Set the grid position to be within the tower's range
    test_enemy.grid_position = (3, 3)  # within range
    assert test_tower.in_range(test_enemy) is True

    # Set the enemy outside of range
    test_enemy.grid_position = (5, 5)  # outside range
    assert test_tower.in_range(test_enemy) is False


def test_tower_get_target(test_tower, test_enemy):
    """Test the tower's ability to target an enemy."""
    enemies = [test_enemy]
    target = test_tower.get_target(enemies)
    assert target == test_enemy


def test_tower_shoot(test_tower, test_enemy):
    """Test that the tower shoots and adds a bullet to its bullets list."""
    test_tower.target = test_enemy  # Set target to the enemy

    # Before shooting, check the bullets list is empty
    assert len(test_tower.bullets) == 0

    # Perform a shoot action
    test_tower.shoot()

    # Check if a bullet is added
    assert len(test_tower.bullets) == 1
    assert isinstance(test_tower.bullets[0], Bullet)


def test_tower_update(test_tower, test_enemy):
    """Test the update method of the tower."""
    test_tower.target = test_enemy
    initial_bullet_count = len(test_tower.bullets)

    # Update the tower (this should invoke shooting)
    test_tower.update([test_enemy])

    # After update, check if the bullet count has increased
    assert len(test_tower.bullets) > initial_bullet_count


def test_tower_bullet_update(test_tower, test_enemy):
    """Test that bullets are updated correctly."""
    test_tower.target = test_enemy
    test_tower.shoot()

    # Get the first bullet that was fired
    bullet = test_tower.bullets[0]

    # Simulate the bullet becoming inactive
    bullet.active = False

    # Run update to clean up inactive bullets
    test_tower.update([test_enemy])

    # Check if inactive bullets were removed
    assert len(test_tower.bullets) == 0


def test_tower_upgrade(test_tower):
    """Test the abstract upgrade method in a subclass."""
    # Subclass Tower to implement the abstract upgrade method for testing
    class TestTower(BirdFlamethrower):
        def upgrade(self):
            self.bullet_damage += 1
            self.range += 1

    tower = TestTower(x_grid_pos=3, y_grid_pos=3)
    
    # Verify that upgrade increases the bullet damage and range
    initial_bullet_damage = tower.bullet_damage
    initial_range = tower.range
    
    tower.upgrade()

    assert tower.bullet_damage == initial_bullet_damage + 1
    assert tower.range == initial_range + 1
