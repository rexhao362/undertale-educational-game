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

    def get_items(self):
        return self.items
    
    def add_item(self, item):
        self.items.push(item)

    def use_item(self, item):  # use item
        z = None
        for i, object in enumerate(self.items):
            if item.name == object.name:
                z = self.items.pop(i)
        if z.target == 'player':
            z.apply_effect(self.sm.combat.player)
        else:
            z.apply_effect(self.sm.combat.enemy)