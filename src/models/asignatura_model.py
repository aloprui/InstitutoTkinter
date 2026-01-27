from database.quieries import get_connection

class AsignaturaModel:

    @staticmethod
    def crear(nombre, departamento):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO asignaturas (nombre, departamento) VALUES (?, ?)",(nombre,departamento))

    @staticmethod
    def obtener():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asignaturas")
            return cursor.fetchall()

    @staticmethod
    def eliminar(asignatura_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM asignaturas WHERE id = ?""",(asignatura_id,))
