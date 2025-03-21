from States.base_state import State 
from Game.map import Map 
from Entities.Towers.Bird_Flamethrower_tower import BirdFlamethrower
from Entities.Towers.Bomb_tower import Bomb
from Entities.Towers.Laser_tower import Laser
from Entities.Towers.Saw_tower import Saw
from Entities.Towers.Turret_Tower import Turret
class Game_State(State):
    """Main game engine - Manages the in-game logic, events, and rendering"""

    def __init__(self, game):
        """
        Initializes the Game_State.
        
        Args:
            game: Reference to the main game object, allowing access to shared resources.
        """
        super().__init__(game)  # Call the parent State class constructor
        self.map = Map("Marsh_Mallows")
        self.towers={}

        placeholder_towers = [(0, 0, BirdFlamethrower), (8,2, Bomb), (6,3, Laser), (2,3, Saw), (9,9, Turret)]
        for tower in placeholder_towers:
            self.create_tower(*(tower))

    def update(self, events):
        """
        Updates the game based on player input and game logic.
        
        Args:
            events: A list of input events (e.g., keyboard/mouse actions).
        """
        self.handle_events(events)  # Process player input and other events

    def draw(self, screen):
        """
        Handles rendering the game to the screen.

        Args:
            screen: pygame display surface
        """
        self.map.draw(screen) # Draw Map
        self.draw_towers(screen)
    
    def draw_towers(self, screen):
        for _, tower in self.towers.items():
            tower.draw(screen)


    def handle_events(self, events):
        """
        Handles user input and other event-driven behavior.
        
        Args:
            events: A list of events such as key presses or mouse clicks.
        """
        pass  # Placeholder for event handling logic

    def create_tower(self, grid_x_position, grid_y_position, tower_type):
        self.towers[(grid_x_position, grid_y_position)] = tower_type(grid_x_position, grid_y_position)
        self.map.place_tower(grid_x_position,  grid_y_position)
