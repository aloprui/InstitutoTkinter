import customtkinter as ctk
from tkinter import ttk, messagebox

class MatriculaView:
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("Matriculas Instituto")
        self.root.geometry("800x500")

        self.alumno_id_var = ctk.StringVar()
        self.año_var = ctk.StringVar()


        self.build_ui()

    def build_ui(self):
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=10)

        ctk.CTkLabel(frame, text="Alumno(id)").grid(row = 0, column = 0)
        ctk.CTkEntry(frame, textvariable = self.alumno_id_var).grid(row = 0, column=1)

        ctk.CTkLabel(frame, text="Año Academico").grid(row = 1, column = 0)
        ctk.CTkEntry(frame, textvariable=self.año_var).grid(row = 1, column=1)

        ctk.CTkButton(frame, text="Crear", command=self.controller.crear_matricula).grid(row=2, column=0, pady=10)
        ctk.CTkButton(frame, text="Borrar", command=self.controller.borrar_matricula).grid(row=2, column=1)

        self.tree = ttk.Treeview(self.root, columns=("id","nombre","apellido","año_academico"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(fill="both", expand=True, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            self.controller.seleccionar_matricula(values)

    def get_from_data(self):
        self.alumno_id_var.get(), self.año_var.get()

    def limpiar_formulario(self):
        self.alumno_id_var.set("")
        self.año_var.set("")

    def mostrar_matriculas(self, matriculas):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for matricula in matriculas:
            self.tree.insert("", "end", values=matricula)

    def show_error(self, msg):
        messagebox.showerror("Error", msg)

    def show_mensage(self, title, msg):
        messagebox.showinfo(title, msg)

    def run(self):
        self.root.mainloop()