from database.quieries import get_connection
class AlumnoModel:

    @staticmethod
    def crear(persona_id):
        with get_connection() as conn:
            conn.cursor().execute("INSERT OR IGNORE INTO alumnos (persona_id) VALUES (?)", (persona_id,))
            conn.commit()

    @staticmethod
    def obtener():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT personas.id, personas.nombre, personas.apellido, personas.dni,
                       personas.telefono, personas.email
                FROM alumnos
                JOIN personas ON alumnos.persona_id = personas.id""")
            return cursor.fetchall()

    @staticmethod
    def borrar(persona_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM alumnos WHERE persona_id = ?""", (persona_id,))
            cursor.execute("""DELETE FROM personas WHERE id = ?""", (persona_id,))