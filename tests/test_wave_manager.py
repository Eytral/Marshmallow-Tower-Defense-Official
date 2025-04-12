import pytest
from unittest.mock import MagicMock, patch
from Game.Managers.wave_manager import WaveManager
from Game.Core.game_data import GAME_DATA



@pytest.fixture
def mock_game_state():
    """Fixture to mock the game state and enemy manager."""
    mock_enemy_manager = MagicMock()
    mock_enemy_manager.create_enemy = MagicMock()
    mock_enemy_manager.enemies = []

    mock_game_state = MagicMock()
    mock_game_state.enemy_manager = mock_enemy_manager
    return mock_game_state


@pytest.fixture
def wave_manager(mock_game_state):
    """Fixture to create a WaveManager instance."""
    return WaveManager(mock_game_state)


def test_wave_manager_initialization(wave_manager):
    """Test initialization of the WaveManager."""
    assert wave_manager.difficulty == "Normal"
    assert wave_manager.wave_number == 0
    assert wave_manager.spawn_interval == GAME_DATA["Normal"]["Default_Spawn_Interval"]
    assert wave_manager.spawn_cooldown == 0
    assert wave_manager.wave_ongoing is False
    assert wave_manager.enemy_spawn_queue == []


def test_create_enemy_spawn_queue(wave_manager):
    """Test the creation of the enemy spawn queue."""
    spawn_wave = {
        "marshmallow enemy": 3,
        "dark_chocolate enemy": 2
    }
    wave_manager.create_enemy_spawn_queue(spawn_wave)

    assert len(wave_manager.enemy_spawn_queue) == 5
    assert wave_manager.enemy_spawn_queue.count("marshmallow enemy") == 3
    assert wave_manager.enemy_spawn_queue.count("dark_chocolate enemy") == 2


def test_initialise_next_spawn_wave(wave_manager):
    """Test the initialization of the next spawn wave."""
    wave_manager.wave_number = 2  # Simulate wave 2
    wave_manager.initialise_next_spawn_wave()

    assert wave_manager.accumulated_spawns["marshmallow enemy"] == GAME_DATA["Normal"]["Default_Spawn"]["marshmallow enemy"] + GAME_DATA["Normal"]["Increment"]["marshmallow enemy"]
    assert wave_manager.accumulated_spawns["dark_chocolate enemy"] == GAME_DATA["Normal"]["Default_Spawn"]["dark_chocolate enemy"] + GAME_DATA["Normal"]["Increment"]["dark_chocolate enemy"]


def test_start_wave(wave_manager):
    """Test the start wave functionality."""
    wave_manager.start_wave()

    assert wave_manager.wave_ongoing is True
    assert wave_manager.enemy_spawn_queue != []


def test_spawn_enemies(wave_manager, mock_game_state):
    """Test spawning of enemies during a wave."""
    wave_manager.create_enemy_spawn_queue({"marshmallow enemy": 2})

    wave_manager.spawn_enemies()

    mock_game_state.enemy_manager.create_enemy.assert_called_once_with("marshmallow enemy")

    assert wave_manager.spawn_cooldown == wave_manager.spawn_interval


def test_next_wave(wave_manager):
    """Test the functionality of starting the next wave."""
    wave_manager.wave_ongoing = False
    wave_manager.next_wave()

    assert wave_manager.wave_number == 1
    assert wave_manager.spawn_interval == GAME_DATA["Normal"]["Default_Spawn_Interval"] - 1
    assert wave_manager.wave_ongoing is True

def test_reset_waves(wave_manager):
    """Test the reset wave functionality."""
    wave_manager.wave_number = 3
    wave_manager.spawn_cooldown = 5
    wave_manager.spawn_interval = 10
    wave_manager.accumulated_spawns = {"marshmallow enemy": 5}
    wave_manager.enemy_spawn_queue = ["marshmallow enemy", "marshmallow enemy"]

    wave_manager.reset_waves()

    assert wave_manager.wave_number == 0
    assert wave_manager.spawn_cooldown == 0
    assert wave_manager.spawn_interval == GAME_DATA["Normal"]["Default_Spawn_Interval"]
    assert wave_manager.enemy_spawn_queue == []
    assert wave_manager.accumulated_spawns == GAME_DATA["Normal"]["Default_Spawn"]
