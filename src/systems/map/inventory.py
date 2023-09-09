from src.systems.state import State


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
        return [item.name for item in self.items]

    def add_item(self, item, success):
        if success:
            self.items.append(item)

    def use_item(self, item_name, success):
        item_to_use = None
        for i, object in enumerate(self.items):
            if item_name == object.name:
                item_to_use = self.items.pop(i)
        if success:
            if item_to_use.target == 'player':
                item_to_use.apply_effect(self.sm.player)
                text = [f'You have used {item_to_use.name}',
                        f"""It has increased your {item_to_use.attribute}
                        by {item_to_use.effect}"""]
                self.sm.player.text_entry.extend(text)
            else:
                item_to_use.apply_effect(self.sm.state.enemy)
                text = [f'You have used {item_to_use.name}',
                        f"""It has decreased {self.sm.state.enemy}'s
                        {item_to_use.attribute} by {item_to_use.effect}"""]
                self.sm.player.text_entry.extend(text)
        else:
            text = [f'You have used {item_to_use.name}',
                    'Unfortunately, you failed the quiz, so it did not work']
            self.sm.player.text_entry.extend(text)
