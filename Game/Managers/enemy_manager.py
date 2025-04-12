from Game.Core.game_data import ENEMY_CLASS_MAP

class EnemyManager():
    """
    Manages the active enemies in the game, including updating, creating, and drawing enemies.
    """
    def __init__(self, game_state):
        """
        Initializes the EnemyManager with the given game state and an empty list for active enemies.

        Args:
            game_state: The current state of the game, which contains all game data.
        """
        self.game_state = game_state
        self.enemies = []  # List to store active enemies

    def update_enemies(self):
        """
        Updates each enemy's movement and removes dead or finished enemies from the list.

        Loops through all active enemies, calling the update method for each, and removes enemies that are no longer active.
        """
        for enemy in self.enemies:
            enemy.update(self.game_state)  # Update each enemy's state

    def create_enemy(self, enemy_name, **kwargs):
        """
        Creates and adds an enemy to the game based on the provided enemy name and optional parameters.

        Args:
            enemy_name (str): The name of the enemy to create.
            kwargs: Optional keyword arguments for custom starting position and path.
        """
        if kwargs:
            # If custom parameters are provided, use them for the enemy's starting position and path
            start_position = kwargs["Start_Position"]
            enemy_path = kwargs["Path"]
        else:
            # Otherwise, use the default values from the game state
            start_position = self.game_state.map.enemy_start_pos
            enemy_path = self.game_state.map.enemy_path
        print(f"Created enemy {enemy_name}")
        
        # Get the appropriate enemy class from the class map
        enemy_class = ENEMY_CLASS_MAP.get(enemy_name)
        if enemy_class:
            # If the enemy class exists, create an instance and add it to the list of enemies
            self.enemies.append(enemy_class(start_position, enemy_path))

    def draw_enemies(self, screen):
        """
        Draws all active enemies on the screen.

        Args:
            screen: The screen to draw the enemies on.
        """
        for enemy in self.enemies:
            enemy.draw(screen)  # Draw each enemy on the screen
    
    def draw(self, screen):
        """
        Draws all enemies by calling the draw_enemies method.

        Args:
            screen: The screen to draw the enemies on.
        """
        self.draw_enemies(screen)  # Draws all enemies
