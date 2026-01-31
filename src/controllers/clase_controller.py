from src.views.clase_view import ClaseView
from src.models.clase_model import ClaseModel

class ClaseController:
    def __init__(self):
        self.view = ClaseView(self)
        self.clase_seleccionada_id = None
        self.car_clases()

    def car_clases(self):
        clases = ClaseModel().obtener()
        self.view.mostrar_clases(clases)

    def crear_clase(self):
        profesor_id, aula_id, asignatura_id, año = self.view.get_from_data()

        if not profesor_id or not aula_id or not asignatura_id or not año:
            self.view.show_error("Todos los campos son obligatorios")
            return

        try:
            ClaseModel.crear(profesor_id, aula_id, asignatura_id, año)
            self.view.show_mensage("Clase creada exitosamente")
            self.view.limpiar_formulario()
            self.car_clases()
        except Exception as e:
            self.view.show_error(str(e))

    def seleccionar_clase(self, values):
        self.clase_seleccionada_id = values[0]
        self.view.cargar_formulario(values)

    def actualizar_clase(self):
        if not self.clase_seleccionada_id:
            self.view.show_error("Seleccione una clase.")
            return

        profesor_id, aula_id, asignatura_id, año = self.view.get_from_data()
        if not profesor_id or not aula_id or not asignatura_id or not año:
            self.view.show_error("Todos los campos son obligatorios")
            return

        try:
            ClaseModel.actualizar(self.clase_seleccionada_id, profesor_id, aula_id, asignatura_id, año)
            self.view.show_mensage("Clase actualizada exitosamente")
            self.view.limpiar_formulario()
            self.clase_seleccionada_id = None
            self.car_clases()
        except Exception as e:
            self.view.show_error(str(e))

    def borrar_clase(self):
        if not self.clase_seleccionada_id:
            self.view.show_error("Seleccione una clase.")
            return

        try:
            ClaseModel.eliminar(self.clase_seleccionada_id)
            self.view.show_mensage("Clase eliminada exitosamente")
            self.view.limpiar_formulario()
            self.clase_seleccionada_id = None
            self.car_clases()
        except Exception as e:
            self.view.show_error(str(e))

    def run(self):
        self.view.run()