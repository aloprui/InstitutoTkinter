from src.views.login_view import LoginView

from src.models.usuario_model import UsuarioModel

from tkinter import messagebox

class LoginController:
    def __init__(self):
        self.view = LoginView(self)

    def login(self):
        usuario, pasword = self.view.get_credentials()

        if not usuario or not pasword:
            self.view.show_error("Todos los campos son obligatorios.")
            return
        usuario_db = UsuarioModel.verificar(usuario, pasword)

        if usuario_db:
            messagebox.showinfo("Bienvenido," " Login correcto.")
            self.view.close()


            #Meter ahora menu_controller
            from src.controllers.menu_controllet import MenuController
            self.menu = MenuController()
            self.menu.run()
        else:
            self.view.show_error("Usuario no existe o contraseña no existe")

    def run(self):
        self.view.run()