import customtkinter as ctk
from tkinter import ttk, messagebox, StringVar


class MaterialView():
    def __init__(self,controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("Material Instituto")
        self.root.geometry("800x500")

        self.nombre_var = ctk.StringVar()
        self.descripcion_var = ctk.StringVar()
        self.aula_id_var = ctk.StringVar()

        self.build_ui()

    def build_ui(self):
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady = 10)

        ctk.CTkLabel(frame, text="Nombre").grid(row = 0, column = 0)
        ctk.CTkEntry(frame, textvariable = self.nombre_var).grid(row = 0, column = 1)

        ctk.CTkLabel(frame, text="Descripcion").grid(row = 1, column = 0)
        ctk.CTkEntry(frame, textvariable = self.descripcion_var).grid(row = 1, column=1)

        ctk.CTkLabel(frame, text="Aula(id)").grid(row = 2, column = 0)
        ctk.CTkEntry(frame, textvariable = self.aula_id_var).grid(row = 2, column=1)

        ctk.CTkButton(frame, text="Crear", command=self.controller.crear_materiales).grid(row=3, column=0, pady=10)
        ctk.CTkButton(frame, text="Actualizar", command=self.controller.actualizar_materiales).grid(row=3, column=1)
        ctk.CTkButton(frame, text="Borrar", command=self.controller.borrar_materiales).grid(row=4, column=2, columnspan=2)

        self.tree = ttk.Treeview(self.root, columns=("id","nombre","descripcion","aula_id"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text = col.capitalize())
        self.tree.pack(fill="both", expand=True, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.on_selct)

    def on_selct(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            self.controller.seleccionar_material(values)

    def get_from_data(self):
        return self.nombre_var.get(), self.descripcion_var.get(), self.aula_id_var.get()

    def cargar_formulario(self, values):
        self.nombre_var.set(values[1])
        self.descripcion_var.set(values[2])
        self.aula_id_var.set(values[3])

    def limpar_formulario(self):
        self.nombre_var.set("")
        self.descripcion_var.set("")
        self.aula_id_var.set("")

    def mostrar_materiales(self, materiales):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for material in materiales:
            self.tree.insert('', 'end', values=material)

    def show_error(self, msg):
        messagebox.showerror("Error", msg)

    def show_mensage(self, title, msg):
        messagebox.showinfo(title, msg)

    def run(self):
        self.root.mainloop()