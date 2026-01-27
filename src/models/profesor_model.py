from database.quieries import get_connection

class ProfesorModel:

    @staticmethod
    def crear(persona_id, departamento):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO profesores(persona_id, departamento)
                        VALUES(?,?)""", (persona_id, departamento))

    @staticmethod
    def obtener():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT personas.id, personas.nombre, personas.apellido, personas.dni,
                        personas.telefono, personas.email, profesores.departamento
                        FROM profesores
                        JOIN personas ON profesores.persona_id = personas.id""")
        return cursor.fetchall()

    @staticmethod
    def eliminar(persona_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM profesores WHERE persona_id = ?""", (persona_id,))
            cursor.execute("""DELETE FROM personas WHERE id = ?""", (persona_id,))