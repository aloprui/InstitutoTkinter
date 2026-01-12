import customtkinter as ctk

class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SALUDAR")
        self.geometry("400x300")

        self._crear_widgets()

    def _crear_widgets(self):
        """Crear elementos gráficos"""

        self.label = ctk.CTkLabel(self, text="Saludar", font=("Arial", 20))
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Saludar", command=self.saludar)
        self.button.pack(pady=20)

    def saludar(self):
        self.label.configure(text="HOLA")