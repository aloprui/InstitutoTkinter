from src.models.aula_model import AulaModel
from src.views.asignatura_view import AsignaturaView
from src.models.asignatura_model import AsignaturaModel

class AsignaturaController:
    def __init__(self):
        self.view = AsignaturaView(self)
        self.asignatura_seleccionada_id = None
        self.cargar_asignaturas()


    def cargar_asignaturas(self):
        asignaturas = AsignaturaModel().obtener()
        self.view.mostrar_asignatura(asignaturas)

    def crear_asignatura(self):
        nombre, departamento = self.view.get_from_data()

        if not nombre or not departamento:
            self.view.show_mensage("Todos los campos son obligatorios")
            return

        try:
            AsignaturaModel.crear(nombre, departamento)
            self.view.show_mensage("Asignatura creada exitosamente")
            self.view.limpiar_formulario()
            self.cargar_asignaturas()
        except Exception as e:
            self.view.show_error(str(e))

    def seleccionar_asignatura(self, values):
        self.asignatura_seleccionada_id =values[0]
        self.view.cargar_formulario(values)

    def actualizar_asignatura(self):
        if not self.asignatura_seleccionada_id:
            self.view.show_error("No se ha seleccionado ninguna asignatura")
            return

        nombre, departamento = self.view.get_from_data()

        if not nombre or not departamento:
            self.view.show_mensage("Todos los campos son obligatorios")
            return

        try:
            AulaModel.actualizar(self.asignatura_seleccionada_id,nombre, departamento)
            self.view.show_mensage("Asignatura actualizada")
            self.view.limpiar_formulario()
            self.asignatura_seleccionada_id = None
            self.cargar_asignaturas()
        except Exception as e:
            self.view.show_error(str(e))

    def borrar_asignatura(self):
        if not self.asignatura_seleccionada_id:
            self.view.show_error("No se ha seleccionado ninguna asignatura")
            return

        try:
            AsignaturaModel.eliminar(self.asignatura_seleccionada_id)
            self.view.show_mensage("Asignatura borrada")
            self.view.limpiar_formulario()
            self.asignatura_seleccionada_id = None
            self.cargar_asignaturas()
        except Exception as e:
            self.view.show_error(str(e))

    def run(self):
        self.view.run()