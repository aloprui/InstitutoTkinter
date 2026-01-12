import tkinter as tk

def saludar():
    etiqueta.config(text="¡Hola Mundo!")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi primer programa en Tkinter")
ventana.geometry("400x200")

# Etiqueta
etiqueta = tk.Label(ventana, text="Presiona el botón", font=("Arial", 12))
etiqueta.pack(pady=20)

# Botón
boton = tk.Button(
    ventana,
    text="Saludar",
    command=saludar
)
boton.pack()

# Ejecutar la app
ventana.mainloop()
