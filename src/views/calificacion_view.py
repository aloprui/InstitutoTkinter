import customtkinter as ctk
from tkinter import ttk, messagebox

class CalificacionesView:
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("Calificaciones Instituto")
        self.root.geometry("800x500")

        self.alumno_id_var = ctk.StringVar()
        self.asignatura_id_var = ctk.StringVar()
        self.convocatoria_id_var = ctk.StringVar()
        self.nota_var = ctk.StringVar()
        self.año_var = ctk.StringVar()

        self.build_ui()

    def build_ui(self):
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=10)

        ctk.CTkLabel(frame, text="Alumno(id)").grid(row = 0, column = 0)
        ctk.CTkEntry(frame, textvariable = self.alumno_id_var).grid(row = 0, column=1)

        ctk.CTkLabel(frame, text="Asignatura(id)").grid(row = 1, column = 0)
        ctk.CTkEntry(frame, textvariable = self.asignatura_id_var).grid(row = 1, column=1)

        ctk.CTkLabel(frame, text="Convocatoria(id)").grid(row = 2, column = 0)
        ctk.CTkEntry(frame, textvariable = self.convocatoria_id_var).grid(row = 2, column=1)

        ctk.CTkLabel(frame, text="Nota").grid(row = 3, column = 0)
        ctk.CTkEntry(frame, textvariable = self.nota_var).grid(row = 3, column=1)

        ctk.CTkLabel(frame, text="Año Academico").grid(row = 4, column = 0)
        ctk.CTkEntry(frame, textvariable=self.año_var).grid(row = 4, column=1)

        ctk.CTkButton(frame, text="Crear", command=self.controller.crear_calificacion).grid(row=5, column=0, pady=10)
        ctk.CTkButton(frame, text="Borrar", command=self.controller.borrar_calificacion).grid(row=5, column=1)

        self.tree = ttk.Treeview(self.root, columns=("id","nombre", "apellido","asignatura", "convocatoria", "nota","año"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(fill="both", expand=True, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            self.controller.seleccionar_calificacion(values)

    def get_from_data(self):
        return( self.alumno_id_var.get(), self.asignatura_id_var.get(),
                self.convocatoria_id_var.get(), self.nota_var.get(), self.año_var.get())

    def limpiar_formulario(self):
        self.alumno_id_var.set("")
        self.asignatura_id_var.set("")
        self.convocatoria_id_var.set("")
        self.nota_var.set("")
        self.año_var.set("")

    def mostrar_calificaciones(self, calificaciones):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for calificacion in calificaciones:
            self.tree.insert("","end",values=calificacion)

    def show_error(self, msg):
        messagebox.showerror("Error", msg)

    def show_mensage(self, title, msg):
        messagebox.showinfo(title, msg)

    def run(self):
        self.root.mainloop()