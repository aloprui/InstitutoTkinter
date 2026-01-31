from database.quieries import get_connection

class PersonaModel:
    @staticmethod
    def crear(nombre,apellido, dni, telefono, email):
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO personas(nombre, apellido, dni, telefono,email)
                            VALUES(?,?,?,?,?)""",(nombre, apellido, dni, telefono, email))
            return cursor.lastrowid

    @staticmethod
    def actualizar(persona_id, nombre, apellido, dni, telefono, email):
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE personas
            SET nombre = ?, apellido = ?, dni = ?, telefono = ?, email = ?
            WHERE id=?""", (nombre, apellido, dni, telefono, email, persona_id))

    @staticmethod
    def eliminar(persona_id):
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM personas
            WHERE id=?""", (persona_id,))

    @staticmethod
    def obtener_todas():
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT id, nombre, apellido, dni, telefono, email 
                FROM personas""")
            return cursor.fetchall()