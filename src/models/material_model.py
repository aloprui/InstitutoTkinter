from database.quieries import get_connection

class MaterialModel:
    @staticmethod
    def crear(nombre, descripcion, aula_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO materiales (nombre, descripcion, aula_id)
                            VALUES (?, ?, ?)""",(nombre,descripcion,aula_id))


    @staticmethod
    def obtener():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT materiales.id, materiales.nombre, materiales.descripcion, aulas.numero 
            FROM materiales 
            JOIN aulas ON aulas.id = materiales.aula_id""")
        return cursor.fetchall()


    @staticmethod
    def eliminar(material_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM materiales WHERE id = ?""",(material_id,))
