from src.state_manager import StateManager
current_user = ['player']


def run_app():
    app = StateManager(current_user[0])
    app.run(screen, manager)


if __name__ == '__main__':
    run_app()
