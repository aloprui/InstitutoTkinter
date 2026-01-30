import customtkinter as ctk
from tkinter import ttk, messagebox

class ClaseView:
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("Clases Instituto")
        self.root.geometry("800x500")


        self.profesor_id_var = ctk.StringVar()
        self.aula_id_var = ctk.StringVar()
        self.asignatura_id_var = ctk.StringVar()
        self.año_var = ctk.StringVar()


        self.build_ui()

    def build_ui(self):
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=10)

        ctk.CTkLabel(frame, text="Profesor(id)").grid(column=0, row=0)
        ctk.CTkEntry(frame, textvariable=self.profesor_id_var).grid(column=1, row=0)

        ctk.CTkLabel(frame, text="Aula(id)").grid(column=0, row=1)
        ctk.CTkEntry(frame, textvariable=self.aula_id_var).grid(column=1, row=1)

        ctk.CTkLabel(frame, text="Asignatura(id)").grid(column=0, row=2)
        ctk.CTkEntry(frame, textvariable=self.asignatura_id_var).grid(column=1, row=2)

        ctk.CTkLabel(frame, text="Año").grid(column=0, row=3)
        ctk.CTkEntry(frame, textvariable=self.año_var).grid(column=1, row=3)

        ctk.CTkButton(self.root, text="Crear", command=self.controller.crear_aula).grid(row=4, column=0, pady=10)
        ctk.CTkButton(self.root, text="Actualizar", command=self.controller.actualizar_aula).grid(row=4, column=1)
        ctk.CTkButton(self.root, text="Borrar", command=self.controller.borrar_aula).grid(row=5, column=0, columnspan=2)

        self.tree = ttk.Treeview(self.root, columns=("id", "profesor_id", "aula_id", "asignatura_id", "año_var"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(fill="both", expand=True, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            self.controller.seleccionar_clase(values)

    def get_from_data(self, values):
        self.profesor_id_var.set(values[1])
        self.aula_id_var.set(values[2])
        self.asignatura_id_var.set(values[3])
        self.año_var.set(values[4])

    def limpiar_formulario(self):
        self.profesor_id_var.set("")
        self.aula_id_var.set("")
        self.asignatura_id_var.set("")
        self.año_var.set("")

    def mostrar_clases(self, clases):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for clase in clases:
            self.tree.insert("","end", values=clase)

    def run(self):
        self.root.mainloop()