from src.views.aula_view import AulaView

from src.models.aula_model import AulaModel

class AulaController:
    def __init__(self):
        self.view = AulaView(self)
        self.aula_seleccionada_id = None
        self.cagar_aula()

    def cagar_aula(self):
        aulas = AulaModel().obtener()
        self.view.mostrar_aulas(aulas)

    def crear_aula(self):
        numero, capacidad = self.view.get_from_data()

        if not numero or capacidad:
            self.view.show_error("Todos los campos son obligatorios.")
            return

        try:
            AulaModel.create(numero, capacidad)
            self.view.show_mensage("Exito","Aula creada con Éxito.")
            self.view.limpiar_formulario()
            self.cagar_aula()
        except Exception as e:
            self.view.show_error(str(e))

    def seleccionar_aula(self, values):
        self.aula_seleccionada_id = values[0]
        self.view.cargar_formularios(values)

    def actualizar_aula(self):
        if not self.aula_seleccionada_id:
            self.view.show_error("Aula selecionada incorrecta.")
            return

        numero, capacidad = self.view.get_from_data()

        if not numero or capacidad:
            self.view.show_error("Todos los campos son obligatorios.")
            return
        try:
            AulaModel.actualizar(self.aula_seleccionada_id, numero, capacidad)
            self.view.show_mensage("Exito", " Aula actualizada con exito.")
            self.view.limpiar_formulario()
            self.aula_seleccionada_id = None
            self.cagar_aula()
        except Exception as e:
            self.view.show_error(str(e))

    def borrar_aula(self):
        if not self.aula_seleccionada_id:
            self.view.show_error("Aula selecionada incorrecta.")
            return

        try:
            AulaModel.borrar(self.aula_seleccionada_id)
            self.view.show_mensage("Exito", " Aula borrada con exito.")
            self.view.limpiar_formulario()
            self.aula_seleccionada_id = None
            self.cagar_aula()
        except Exception as e:
            self.view.show_error(str(e))

    def run(self):
        self.view.run()