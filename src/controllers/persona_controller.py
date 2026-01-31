from src.views.persona_view import PersonaView
from src.models.persona_model import PersonaModel

from tkinter import messagebox

class PersonaController:
    def __init__(self):
        self.view = PersonaView(self)
        self.persona_seleccionada_id = None
        self.cargar_personas()

    def cargar_personas(self):
        personas = PersonaModel().obtener_todas()
        self.view.mostrar_persona(personas)

    def crear_persona(self):
        nombre, apellido, dni, telefono, email = self.view.get_from_data()

        if not nombre or not apellido or not dni:
            self.view.show_error("Nombre, apellido y DNI son obligatorios.")


        try:
            PersonaModel.crear(nombre, apellido, dni, telefono, email)
            self.view.show_mensage("Exito", "Persona creada con exito.")
            self.view.limpiar_formulario()
            self.cargar_personas()
        except Exception as e:
            self.view.show_error(str(e))

    def seleccionar_persona(self, values):
        self.persona_seleccionada_id = values[0]
        self.view.cargar_formulario(values)

    def hacer_alumno(self):
        if not self.persona_seleccionada_id:
            return self.view.show_error("Selecciona a una persona primero.")
        try:
            from src.models.alumno_model import AlumnoModel
            AlumnoModel.crear(self.persona_seleccionada_id)
            self.view.show_mensage("Éxito", "Registrado como Alumno correctamente.")
        except Exception as e:
            self.view.show_error(f"Error al registrar alumno: {e}")

    def hacer_profesor(self):
        if not self.persona_seleccionada_id:
            return self.view.show_error("Selecciona a una persona primero.")
        try:
            from src.models.profesor_model import ProfesorModel
            # Asignamos un departamento por defecto
            ProfesorModel.crear(self.persona_seleccionada_id, "Informatica")
            self.view.show_mensage("Éxito", "Registrado como Profesor correctamente.")
        except Exception as e:
            self.view.show_error(f"Error al registrar profesor: {e}")

    def hacer_directivo(self):
        if not self.persona_seleccionada_id:
            return self.view.show_error("Selecciona a una persona primero.")
        try:
            from src.models.direccion_model import DireccionModel
            # 'Secretario' es un cargo válido según tu CHECK de la base de datos
            DireccionModel.crear(self.persona_seleccionada_id, "Secretario")
            self.view.show_mensage("Éxito", "Registrado en Dirección correctamente.")
        except Exception as e:
            self.view.show_error(f"Error al registrar directivo: {e}")

    def actualizar_persona(self):
        if not self.persona_seleccionada_id:
            self.view.show_error("Selecciona a una persona.")
            return

        nombre, apellido, dni, telefono, email = self.view.get_from_data()

        if not nombre or not apellido or not dni:
            self.view.show_error("Nombre, apellido y DNI son obligatorios.")
            return

        try:
            PersonaModel.actualizar(self.persona_seleccionada_id, nombre, apellido, dni, telefono, email)
            self.view.show_mensage("Exito", "Persona actualizada con exito.")
            self.view.limpiar_formulario()
            self.persona_seleccionada_id = None
            self.cargar_personas()
        except Exception as e:
            self.view.show_error(str(e))

    def borrar_persona(self):
        if not self.persona_seleccionada_id:
            self.view.show_error("Selecciona a una persona.")
            return
        try:
            PersonaModel.eliminar(self.persona_seleccionada_id)
            self.view.show_mensage("Exito", "Persona borrada con exito.")
            self.view.limpiar_formulario()
            self.persona_seleccionada_id = None
            self.cargar_personas()
        except Exception as e:
            self.view.show_error(str(e))

    def run(self):
        self.view.run()