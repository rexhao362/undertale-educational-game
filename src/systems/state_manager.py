class StateManager:
    def __init__(self, state):
        self.current_state = state
        self.previous_state = None

    def next_state(self, new_state):
        self.previous_state = self.current_state
        self.current_state = new_state

    def back_state(self):
        self.current_state = self.previous_state