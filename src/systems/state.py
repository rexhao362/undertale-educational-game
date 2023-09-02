class State:
    def __init__(self, state_manager):
        self.sm = state_manager
        self.reward = None

    def draw(self, screen, time_delta):
        pass

    def update(self):
        pass

    def events(self, manager):
        pass

    def reward_check(self):
        if self.reward != None:
            if self.sm.get_success():
                self.reward()
            elif not self.sm.get_success():
                pass
            self.reward = None
            self.sm.set_success(None)

    def success_check(self):
        if self.sm.get_success():
            pass
            # self.sm.set_success(False)

    def store_state(self):
        pass
