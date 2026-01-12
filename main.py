import customtkinter as ctk
from src.views.main_view import MainView


def ventanaSaludo():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = MainView()
    app.mainloop()


if __name__ == '__main__':
    ventanaSaludo()

#---
#def saludar():
#    etiqueta.config(text="¡Hola Mundo!")

# Crear ventana principal
#ventana = ctk.Ctk()
#ventana.title("Mi primer programa en Tkinter")
#ventana.geometry("400x200")

# Etiqueta
#etiqueta = ctk.Label(ventana, text="Presiona el botón", font=("Arial", 12))
#etiqueta.pack(pady=20)

# Botón
#boton = ctk.Button(
#    ventana,
#    text="Saludar",
#    command=saludar)
#boton.pack()

# Ejecutar la app
#ventana.mainloop()

#------------