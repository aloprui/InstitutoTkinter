from database.quieries import get_connection

class ConvocatoriaModel:

    @staticmethod
    def crear(nombre):
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO convocatorias(nombre) VALUES (?)""", (nombre,))
            connection.commit()

    @staticmethod
    def obtener():
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM convocatorias""")
            return cursor.fetchall()

    @staticmethod
    def borrar(convocatoria_id):
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM convocatorias WHERE id = ?""", (convocatoria_id,))
            connection.commit()