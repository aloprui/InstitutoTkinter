from src.views.material_view import MaterialView
from src.models.material_model import MaterialModel

class MaterialController:
    def __init__(self):
        self.view = MaterialView(self)
        self.material_seleccionado_id = None
        self.cargar_materiales()

    def cargar_materiales(self):
        materiales = MaterialModel().obtener()
        self.view.mostrar_materiales(materiales)

    def crear_materiales(self):
        nombre, descripcion, aula_id = self.view.get_from_data()

        if not nombre or not  aula_id:
            self.view.show_error("Nombre y Aula son obligatorios")
            return
        try:
            MaterialModel.crear(nombre, descripcion, aula_id)
            self.view.show_mensage("Exito", "Material creado")
            self.view.limpar_formulario()
            self.cargar_materiales()

        except Exception as e:
            self.view.show_error(str(e))

    def seleccionar_material(self, values):
        self.material_seleccionado_id = values[0]
        self.view.cargar_formulario(values)

    def actualizar_materiales(self):
        if not self.material_seleccionado_id:
            self.view.show_error("Selecciona un material para actualizar.")
            return

        nombre, descripcion, aula_id = self.view.get_from_data()

        if not nombre or not aula_id:
            self.view.show_error("Nombre y Aula son obligatorios")
            return
        try:
            MaterialModel.actualizar(self.material_seleccionado_id, nombre, descripcion, aula_id)
            self.view.show_mensage("Exito", "Material actualizado")
            self.view.limpar_formulario()
            self.material_seleccionado_id = None
            self.cargar_materiales()
        except Exception as e:
            self.view.show_error(str(e))

    def borrar_materiales(self):
        if not self.material_seleccionado_id:
            self.view.show_error("Selecciona un material para borrar.")
            return

        try:
            MaterialModel.eliminar(self.material_seleccionado_id)
            self.view.show_mensage("Exito", "Material borrado")
            self.view.limpar_formulario()
            self.material_seleccionado_id = None
            self.cargar_materiales()
        except Exception as e:
            self.view.show_error(str(e))

    def run(self):
        self.view.run()