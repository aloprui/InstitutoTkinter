from database.quieries import get_connection

class MatriculaModel:
    @staticmethod
    def crear(alumno_id, año_academico):
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO matriculas(alumno_id, año_academico)
                                    VALUES (?,?)""", (alumno_id, año_academico))


    @staticmethod
    def ver():
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT matriculas.id, personas.nombre, personas.apellido,
                            matriculas.año_academico FROM matriculas
                            JOIN alumnos ON matriculas.alumno_id = alumnos.persona_id
                            JOIN personas ON alumnos.persona_id = personas.id""")
            return cursor.fetchall()

    @staticmethod
    def eliminar(matricula_id):
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM matriculas WHERE id = ?""", (matricula_id,))