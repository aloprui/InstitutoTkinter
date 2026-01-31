import customtkinter as ctk
from tkinter import ttk, messagebox

class AulaView():
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("Aula - Instituto")
        self.root.geometry("800x500")

        self.numero_var = ctk.StringVar()
        self.capacidad_var = ctk.StringVar()

        self.build_ui()

    def build_ui(self):
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady = 10)

        ctk.CTkLabel(frame, text="Número").grid(row = 0, column = 0)
        ctk.CTkEntry(frame, textvariable = self.numero_var).grid(row = 0, column = 1)

        ctk.CTkLabel(frame, text="Capacidad").grid(row = 1, column = 0)
        ctk.CTkEntry(frame, textvariable = self.capacidad_var).grid(row = 1, column=1)

        ctk.CTkButton(frame, text="Crear", command=self.controller.crear_aula).grid(row=2, column=0, pady=10, padx=5)
        ctk.CTkButton(frame, text="Actualizar", command=self.controller.actualizar_aula).grid(row=2, column=1, pady=10,padx=5)
        ctk.CTkButton(frame, text="Borrar", command=self.controller.borrar_aula).grid(row=3, column=0, columnspan=2,pady=5)

        self.tree = ttk.Treeview(self.root, columns=("id","numero","capacidad"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(fill="both", expand=True, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            self.controller.seleccionar_aula(values)

    def get_from_data(self):
        return self.numero_var.get(), self.capacidad_var.get()

    def cargar_formularios(self, values):
        self.numero_var.set(values[1])
        self.capacidad_var.set(values[2])

    def limpiar_formulario(self):
        self.numero_var.set("")
        self.capacidad_var.set("")

    def mostrar_aulas(self, aulas):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for aula in aulas:
            self.tree.insert("","end", values=aula)

    def show_error(self, msg):
        messagebox.showerror("Error", msg)

    def show_mensage(self, title, msg):
        messagebox.showinfo(title, msg)

    def run(self):
        self.root.mainloop()
