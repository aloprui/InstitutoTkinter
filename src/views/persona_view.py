import customtkinter as ctk
from tkinter import ttk, messagebox

class PersonaView():
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("Personal Instituto")
        self.root.geometry("800x500")

        self.nombre_var = ctk.StringVar()
        self.apellido_var = ctk.StringVar()
        self.dni_var = ctk.StringVar()
        self.telefono_var = ctk.StringVar()
        self.email_var = ctk.StringVar()

        self.build_ui()


    def build_ui(self):
        frame_for = ctk.CTkFrame(self.root)
        frame_for.pack(pady=10)

        ctk.CTkLabel(frame_for, text="Nombre").grid(row=0, column=0)
        ctk.CTkEntry(frame_for, textvariable=self.nombre_var).grid(row=0, column=1)

        ctk.CTkLabel(frame_for, text="Apellido").grid(row=1, column=0)
        ctk.CTkEntry(frame_for, textvariable=self.apellido_var).grid(row=1, column=1)

        ctk.CTkLabel(frame_for, text="DNI").grid(row=2, column=0)
        ctk.CTkEntry(frame_for, textvariable=self.dni_var).grid(row=2, column=1)

        ctk.CTkLabel(frame_for, text="Telefono").grid(row=3, column=0)
        ctk.CTkEntry(frame_for, textvariable=self.telefono_var).grid(row=3, column=1)

        ctk.CTkLabel(frame_for, text="Email").grid(row=4, column=0)
        ctk.CTkEntry(frame_for, textvariable=self.email_var).grid(row=4, column=1)

        ctk.CTkButton(frame_for, text="Crear", command=self.controller.crear_persona).grid(row=5, column=0, pady=10)
        ctk.CTkButton(frame_for, text="Actualizar", command=self.controller.actualizar_persona).grid(row=5, column=1)
        ctk.CTkButton(frame_for, text="Borrar", command=self.controller.borrar_persona).grid(row=5, column=2, pady=5)

        self.tree = ttk.Treeview(self.root,columns=("id","nombre","apellido","dni","telefono","email"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(fill="both", expand=True, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def on_select(self,event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            self.controller.seleccionar_persona(values)

    def get_from_data(self):
        return(self.nombre_var.get(), self.apellido_var.get(), self.dni_var.get(), self.telefono_var.get(),
               self.email_var.get())

    def cargar_formulario(self, values):
        self.nombre_var.set(values[1])
        self.apellido_var.set(values[2])
        self.dni_var.set(values[3])
        self.telefono_var.set(values[4])
        self.email_var.set(values[5])

    def limpiar_formulario(self):
        self.nombre_var.set("")
        self.apellido_var.set("")
        self.dni_var.set("")
        self.telefono_var.set("")
        self.email_var.set("")

    def mostrar_persona(self, personas):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for persona in personas:
            self.tree.insert("", "end", values=persona)

    def run(self):
        self.root.mainloop()