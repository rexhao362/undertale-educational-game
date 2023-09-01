class State:
    def __init__(self):
        self.sm = None
        self.reward = None

    def draw(self, screen, time_delta, manager):
        pass

    def update(self):
        pass

    def events(self, manager):
        pass

    def reward_check(self):
        if self.reward != None:
            if self.sm.get_success():
                self.reward()
                self.reward = None
                self.sm.set_success(None)
            elif not self.sm.get_success():
                self.reward = None
                self.sm.set_success(None)

    def success_check(self):
        if self.sm.get_success():
            pass
            # self.sm.set_success(False)
