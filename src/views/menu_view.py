import customtkinter as ctk

class MenuView:
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("Menu Instituto")
        self.root.geometry("500x500")

        self.build_ui()

    def build_ui(self):
        ctk.CTkLabel(self.root, text="Bienbenido", font=("Verdana", 24)).pack(pady=20)

        ctk.CTkLabel(self.root, text="Menu Instituto", font=("Verdana", 18)).pack(pady=20)

        ctk.CTkButton(self.root, text="Personas", command=self.controller.abrir_personas).pack(pady=5)
        ctk.CTkButton(self.root, text="Aulas", command=self.controller.abrir_aulas).pack(pady=5)
        ctk.CTkButton(self.root, text="Materiales", command=self.controller.abrir_materiales).pack(pady=5)
        ctk.CTkButton(self.root, text="Asignaturas", command=self.controller.abrir_asignaturas).pack(pady=5)
        ctk.CTkButton(self.root, text="Clases", command=self.controller.abrir_clases).pack(pady=5)
        ctk.CTkButton(self.root, text="Matrícula", command=self.controller.abrir_matriculas).pack(pady=5)
        ctk.CTkButton(self.root, text="Calificaciones", command=self.controller.abrir_calificaciones).pack(pady=5)
        ctk.CTkButton(self.root, text="Salir", command=self.controller.salir).pack(pady=15)

    def run(self):
        self.root.mainloop()