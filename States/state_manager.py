from States.base_state import State

class StateManager:
    """
    Manages different game states and handles state transitions.
    This class facilitates switching between different game states, updating 
    the current state, and rendering the active state's visuals.
    """

    def __init__(self):
        """
        Initializes the state manager with an empty set of states and no active state.

        Args:
            states (dict): A dictionary storing states by name.
            current_state (State or None): Tracks the currently active state.
        """
        self.states = {}  # Dictionary to store states by name
        self.current_state = None  # Tracks the currently active state

    def add_state(self, state_name, state):
        """
        Adds a new state to the state manager.

        Args:
            state_name (str): The name of the new state to be added.
            state (State): The state object to add to the manager.
        
        Raises:
            TypeError: If the state is not a subclass of the BaseState class.
        """
        if not isinstance(state, State):
            raise TypeError(f"State '{state_name}' must be a subclass of BaseState")
        
        self.states[state_name] = state  # Add the state to the states dictionary

    def change_state(self, new_state, *args, **kwargs):
        """
        Changes the current game state by transitioning to a new one.

        Args:
            new_state (str): The name of the new state to switch to.
        
        If a transition occurs, it calls the `exit()` method on the current state (if any)
        and the `enter()` method on the new state.
        """
        if new_state in self.states:
            if self.current_state:
                self.current_state.exit(*args, **kwargs)  # Exit the current state before switching

            self.current_state = self.states[new_state]  # Switch to the new state
            self.current_state.enter(*args, **kwargs)  # Initialize the new state
        else:
            print(f"Warning: Attempted to change to unknown state '{new_state}'")  # Log a warning if the state is not found

    def update(self, events):
        """
        Updates the current game state.

        Args:
            events (list): A list of events (e.g., input events) to process.
        
        Calls the `update()` method of the current state, passing along any events.
        """
        if self.current_state:
            self.current_state.update(events)  # Update the current state with the events

    def draw(self, screen, *args):
        """
        Draws the current game state to the screen.

        Args:
            screen (pygame.Surface): The surface (screen) where the game is rendered.
        
        Calls the `draw()` method of the current state to render it on the screen.
        """
        if self.current_state:
            self.current_state.draw(screen)  # Render the current state's visuals
            self.current_state.display_debug_info(screen, *args)  # Optionally display debug info

    def get_current_state(self):
        """
        Returns the name of the current active state.

        Returns:
            str or None: The name of the current state, or None if no state is active.
        """
        return next((name for name, state in self.states.items() if state == self.current_state), None)

    def reset_state(self, *args, **kwargs):
        """
        Reinitializes the current state by calling its exit() and enter() methods.

        This method is useful for resetting the current state without switching to a new one.
        """
        if self.current_state:
            self.current_state.exit(*args, **kwargs)  # Exit the current state
            self.current_state.enter(*args, **kwargs)  # Reinitialize the current state
