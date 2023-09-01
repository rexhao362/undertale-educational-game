class StateManager:
    def __init__(self):#, state):
        self.state = None #state
        self.previous_state = None
        self.success = None

    def next_state(self, new_state):
        self.previous_state = self.state
        self.state = new_state

    def back_state(self):
        self.state = self.previous_state
        
    def set_success(self, bool):
        self.success = bool

    def get_success(self):
        return self.success