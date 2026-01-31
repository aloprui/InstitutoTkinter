from database.quieries import get_connection

class ClaseModel:

    @staticmethod
    def crear(profesor_id, aula_id, asignatura_id, anio_academico):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                   INSERT INTO clases(profesor_id, aula_id, asignatura_id, anio_academico)
                   VALUES (?, ?, ?, ?)
               """, (profesor_id, aula_id, asignatura_id, anio_academico))

    @staticmethod
    def actualizar(clase_id, profesor_id, aula_id, asignatura_id, anio_academico):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE clases 
                    SET profesor_id = ?, aula_id = ?, asignatura_id = ?, anio_academico = ? 
                    WHERE id = ?""", (profesor_id, aula_id, asignatura_id, anio_academico, clase_id))

    @staticmethod
    def obtener():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                   SELECT clases.id, personas.nombre, personas.apellido,
                          asignaturas.nombre, aulas.numero, clases.anio_academico
                   FROM clases
                   JOIN profesores ON clases.profesor_id = profesores.id
                   JOIN personas ON profesores.persona_id = personas.id
                   JOIN asignaturas ON clases.asignatura_id = asignaturas.id
                   JOIN aulas ON clases.aula_id = aulas.id
               """)
            return cursor.fetchall()

    @staticmethod
    def eliminar(clase_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clases WHERE id = ?", (clase_id,))