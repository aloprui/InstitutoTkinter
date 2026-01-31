from database.quieries import init_db

from src.controllers.login_controller import LoginController

if __name__ == '__main__':
    init_db()
    app = LoginController()
    app.run()