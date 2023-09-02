from systems.state import State


class Inventory(State):
    def __init__(self, state_manager):
        super().__init__(state_manager)
        self.items = []

    def draw(self, screen, time_delta):
        pass

    def events(self, manager):
        pass

    def update(self):
        pass