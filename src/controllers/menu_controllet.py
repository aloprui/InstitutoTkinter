from src.views.menu_view import MenuView

class MenuController:
    def __init__(self):
        self.view = MenuView(self)

    def abrir_personas(self):
        from src.controllers.persona_controller import PersonaController
        PersonaController().run()

    def abrir_aulas(self):
        from src.controllers.aula_controller import AulaController
        AulaController().run()

    def abrir_materiales(self):
        from src.controllers.material_controller import MaterialController
        MaterialController().run()

    def abrir_asignaturas(self):
        from src.controllers.asignatura_controller import AsignaturaController
        AsignaturaController().run()

    def abrir_clases(self):
        from src.controllers.clase_controller import ClaseController
        ClaseController().run()

    def abrir_matriculas(self):
        from src.controllers.matricula_controller import MatriculaController
        MatriculaController().run()

    def abrir_calificaciones(self):
        from src.controllers.calificacion_controller import CalificacionController
        CalificacionController().run()

    def salir(self):
        self.view.root.destroy()

    def run(self):
        self.view.run()