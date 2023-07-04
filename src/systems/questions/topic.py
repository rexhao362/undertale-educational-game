from src.run_game import current_subject


class Subject:
    def __init__(self, name, problems):
        self.name = name
    
def set_current_subject(value, subject):
    current_subject[0] = subject