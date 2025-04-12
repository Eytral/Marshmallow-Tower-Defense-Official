import math
import random
from Game.Core.game_data import GAME_DATA

class WaveManager:
    """
    Manages enemy waves in the game.
    """

    def __init__(self, game_state):
        """
        Initializes the WaveManager.

        Args:
            game_state: Reference to the main game object.
        """
        self.difficulty = "Normal"
        self.wave_number = 0  # Tracks the current wave number
        self.spawn_interval = GAME_DATA[self.difficulty]["Default_Spawn_Interval"]
        self.spawn_cooldown = 0  # Countdown timer for enemy spawning
        self.wave_ongoing = False  # Flag indicating whether a wave is currently active
        self.game_state = game_state  # Stores reference to the game instance

        self.accumulated_spawns = {enemy_name: count for enemy_name, count in GAME_DATA[self.difficulty]["Default_Spawn"].items()}
        self.enemy_spawn_queue = []

    def create_enemy_spawn_queue(self, spawn_wave):
        """
        Creates a spawn queue based on the current wave's spawn details.

        Args:
            spawn_wave: Dictionary specifying how many enemies of each type to spawn.
        """
        for enemy_name, count in spawn_wave.items():
            for _ in range(int(count)):
                self.enemy_spawn_queue.append(enemy_name)
        random.shuffle(self.enemy_spawn_queue)

    def initialise_next_spawn_wave(self):
        """
        Initializes the next spawn wave by updating accumulated spawns and creating the spawn queue.
        """
        if self.wave_number > 1:
            for enemy_name, increment in GAME_DATA[self.difficulty]["Increment"].items():
                self.accumulated_spawns[enemy_name] += increment

        spawn_wave = {enemy_name: math.floor(count) for enemy_name, count in self.accumulated_spawns.items()}
        self.create_enemy_spawn_queue(spawn_wave)

    def spawn_enemies(self):
        """
        Spawns enemies at regular intervals if there are enemies left in the spawn queue.
        """
        if self.spawn_cooldown == 0 and self.enemy_spawn_queue:
            enemy_name = self.enemy_spawn_queue.pop(0)  # Spawn the first enemy in the queue
            self.game_state.enemy_manager.create_enemy(enemy_name)  # Create a new enemy at the designated start position
            self.spawn_cooldown = self.spawn_interval  # Reset cooldown timer
        else:
            self.spawn_cooldown -= 1  # Reduce cooldown timer

    def start_wave(self):
        """
        Starts a new wave by initializing the next spawn wave and marking the wave as active.
        """
        self.initialise_next_spawn_wave()
        self.wave_ongoing = True  # Mark the wave as active

    def next_wave(self):
        """
        Starts the next wave if the current one has ended.
        """
        if not self.wave_ongoing:
            self.wave_number += 1  # Increment wave number
            if self.spawn_interval > 5:
                self.spawn_interval -= 1  # Decrease spawn interval to increase wave difficulty
            self.start_wave()  # Start the next wave
        else:
            print(f"Cannot start next wave yet! Current wave is still ongoing.")

    def update(self):
        """
        Updates the wave state, and spawns enemies if a wave is ongoing.
        """
        if self.wave_ongoing:
            if self.enemy_spawn_queue:
                self.spawn_enemies()  # Spawn enemies if there are any in the queue
            else:
                if len(self.game_state.enemy_manager.enemies) == 0:
                    print("All enemies are dead! Wave over.")
                    self.wave_ongoing = False  # Mark the wave as over

    def reset_waves(self):
        """
        Resets all wave-related parameters, typically used when restarting the game.
        """
        self.wave_number = 0
        self.spawn_cooldown = 0
        self.spawn_interval = GAME_DATA[self.difficulty]["Default_Spawn_Interval"]
        self.wave_ongoing = False
        self.accumulated_spawns = {enemy_name: count for enemy_name, count in GAME_DATA[self.difficulty]["Default_Spawn"].items()}
        self.enemy_spawn_queue = []  # Clear Spawn Queue
        print(f"Game reset. Difficulty: {self.difficulty}, Starting wave: {self.wave_number}")
