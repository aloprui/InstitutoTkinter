from src.views.calificacion_view import CalificacionesView
from src.models.calificacion_model import CalificacionModel

class CalificacionController:
    def __init__(self):
        self.view = CalificacionesView(self)
        self.calificacion_seleccionada_id = None
        self.cargar_cali()

    def cargar_cali(self):
        calificacion = CalificacionModel().obtener()
        self.view.mostrar_calificaciones(calificacion)

    def crear_calificacion(self):
        alumno_id, asignatura_id, convocatoria_id, nota, año = self.view.get_from_data()

        if not alumno_id or not asignatura_id or not convocatoria_id or not nota or not año:
            self.view.show_error("Todos los campos son obligatorios.")
            return

        try:
            CalificacionModel.crear(alumno_id, asignatura_id, convocatoria_id, nota, año)
            self.view.show_mensage("Calificaciones creadas")
            self.view.limpiar_formulario()
            self.cargar_cali()
        except Exception as e:
            self.view.show_error(str(e))

    def seleccionar_cali(self, values):
        self.calificacion_seleccionada_id = values[0]

    def borrar_calificacion(self):
        if not self.calificacion_seleccionada_id:
            self.view.show_error("Selecciona una calificacion, para borrar.")
            return

        try:
            CalificacionModel.eliminar(self.calificacion_seleccionada_id)
            self.view.show_mensage("Calificaciones borradas")
            self.view.limpiar_formulario()
            self.calificacion_seleccionada_id = None
            self.cargar_cali()
        except Exception as e:
            self.view.show_error(str(e))

    def run(self):
        self.view.run()