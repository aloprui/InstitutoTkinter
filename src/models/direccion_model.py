from database.quieries import get_connection

class DireccionModel:

    @staticmethod
    def crear(persona_id, cargo):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO profesores(persona_id, cargo) VALUES (?, ?)""", (persona_id, cargo,))

    @staticmethod
    def obtener():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT personas.id, personas.nombre, personas.apellido, personas.dni,
                       personas.telefono, personas.email, direccion.nombre
                       FROM direccion
                       JOIN personas ON direccion.persona_id = personas.id""")

            return cursor.fetchall()


    @staticmethod
    def eliminar(persona_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM direccion WHERE persona_id = ?""", (persona_id,))
            cursor.execute("""DELETE FROM personas WHERE id = ?""", (persona_id,))