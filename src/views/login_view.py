import customtkinter as ctk
from tkinter import messagebox

class LoginView:
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("Login - Instituto Tkinter")
        self.root.geometry("500x500")


        self.usuario_var = ctk.StringVar()
        self.password_var = ctk.StringVar()

        self.build_ui()

    def build_ui(self):
        ctk.CTkLabel(self.root, text="Inicio de sesión", font=("Verdana", 18)).pack(pady=20)

        ctk.CTkLabel(self.root, text="Usuario").pack(pady=20)
        ctk.CTkEntry(self.root, textvariable=self.usuario_var).pack(pady=20)

        ctk.CTkLabel(self.root, text="Password").pack(pady=20)
        ctk.CTkEntry(self.root, textvariable=self.password_var, show="*").pack(pady=20)

        ctk.CTkButton(self.root, text="Entrar", command= self.controller.login).pack(pady=20)

    def get_credentials(self):
        return self.usuario_var.get(), self.password_var.get()

    def show_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    def show_message(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def close(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()