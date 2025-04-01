from States.base_state import State

class StateManager:
    """
    Manages different game states and handles state transitions.
    """

    def __init__(self):
        """
        Initializes the state manager.
        
        Attributes:
            states (dict): A dictionary storing available states by name.
            current_state (State or None): The active game state.
        """
        self.states = {}  # Stores states with their names as keys
        self.current_state = None  # Tracks the active state

    def add_state(self, state_name, state):
        """
        Adds a new state to the state manager.

        Args:
            state_name (str): The name of the state.
            state (State): The state object to add.
        """
        if not isinstance(state, State):
            raise TypeError(f"State '{state_name}' must be a subclass of BaseState")
        self.states[state_name] = state
        self.states[state_name] = state

    def change_state(self, new_state, *args, **kwargs):
        """
        Changes the current game state.

        Args:
            new_state (str): The name of the new state to switch to.

        If a state transition occurs, it calls `exit()` on the old state
        and `enter()` on the new state.
        """
        if new_state in self.states:
            if self.current_state:
                self.current_state.exit(*args, **kwargs)  # Exit the current state

            self.current_state = self.states[new_state]  # Switch to the new state
            self.current_state.enter(*args, **kwargs)  # Initialize the new state
        else:
            print(f"Warning: Attempted to change to unknown state '{new_state}'")  # Or use logging
            return

    def update(self, events):
        """
        Updates the current state.

        Args:
            events (list): A list of events (e.g., input events).
        """
        if self.current_state:
            self.current_state.update(events)  # Call the state's update method

    def draw(self, screen, *args):
        """
        Draws the current state to the screen.

        Args:
            screen: The surface where the game is rendered.
        """
        if self.current_state:
            self.current_state.draw(screen)  # Call the state's draw method
            self.current_state.display_debug_info(screen, *args)

    def get_current_state(self):
        """Returns the name of the current state, or None if no state is active."""
        return next((name for name, state in self.states.items() if state == self.current_state), None)

    def reset_state(self, *args, **kwargs):
        """Reinitializes the current state by calling its exit() and enter() methods."""
        if self.current_state:
            self.current_state.exit(*args, **kwargs)
            self.current_state.enter(*args, **kwargs)