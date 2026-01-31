from database.quieries import get_connection

class CalificacionModel:
    @staticmethod
    def crear(alumno_id, asignatura_id, convocatoria_id, nota, año_academico):
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO calificaciones (alumno_id, asignatura_id, convocatoria_id,
                                nota, año_academico) VALUES (?, ?, ?, ?, ?, ?)""",
                           (alumno_id, asignatura_id, convocatoria_id,nota,año_academico))
            connection.commit()

    @staticmethod
    def obtener():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT c.id, p.nombre, p.apellido, asig.nombre, conv.nombre, c.nota, c.año_academico
                FROM calificaciones c
                JOIN personas p ON c.alumno_id = p.id
                JOIN asignaturas asig ON c.asignatura_id = asig.id
                JOIN convocatorias conv ON c.convocatoria_id = conv.id
            """)
            return cursor.fetchall()


    @staticmethod
    def eliminar(calificacion_id):
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM calificaciones WHERE id = ?""", (calificacion_id,))
            connection.commit()