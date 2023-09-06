from src.state_manager import StateManager
import src.settings as s
import src.manager as m
current_user = ['player']


def run_app():
    app = StateManager(current_user[0])
    app.run(s.screen, m.manager)


if __name__ == '__main__':
    run_app()
