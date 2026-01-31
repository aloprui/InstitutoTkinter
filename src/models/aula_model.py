from database.quieries import get_connection

class AulaModel:

    @staticmethod
    def create(numero, capacidad):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO aulas(numero, capacidad) VALUES (?, ?)""",(numero, capacidad))

    @staticmethod
    def actualizar(aula_id, nuevo_numero, nueva_capacidad):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE aulas 
                    SET numero = ?, capacidad = ? 
                    WHERE id = ?""", (nuevo_numero, nueva_capacidad, aula_id))

    @staticmethod
    def obtener():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM aulas""")
        return cursor.fetchall()

    @staticmethod
    def eliminar(aula_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM aulas WHERE id = ?""",(aula_id,))