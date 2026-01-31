from src.views.matricula_view import MatriculaView
from src.models.matricula_model import MatriculaModel

class MatriculaController:
    def __init__(self):
        self.view = MatriculaView(self)
        self.matricula_seleccionada_id = None
        self.cargar_matricula()

    def cargar_matricula(self):
        matricula = MatriculaModel().ver()
        self.view.mostrar_matriculas(matricula)

    def crear_matricula(self):
        alumno_id, año = self.view.get_from_data()

        if not alumno_id or not año:
            self.view.show_error("Todos los campos son obligatorios.")
            return
        try:
            MatriculaModel.crear(alumno_id, año)
            self.view.show_mensage("Matricula creada exitosamente.")
            self.view.limpiar_formulario()
            self.cargar_matricula()
        except Exception as e:
            self.view.show_error(str(e))

    def seleccionar_matricula(self, values):
        self.matricula_seleccionada_id = values[0]

    def borrar_matricula(self):
        if not self.matricula_seleccionada_id:
            self.view.show_error("Matricula seleccionada inexistente.")
            return
        try:
            MatriculaModel.eliminar(self.matricula_seleccionada_id)
            self.view.show_mensage("Matricula borrada exitosamente.")
            self.view.limpiar_formulario()
            self.matricula_seleccionada_id = None
            self.cargar_matricula()
        except Exception as e:
            self.view.show_error(str(e))

    def run(self):
        self.view.run()