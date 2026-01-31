import sqlite3

DB_NAME = "database.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as connection:
        cursor = connection.cursor()

        #Tabla personas unidas a alumnos, profesores y direccion
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            dni TEXT NOT NULL,
            telefono TEXT,
            email TEXT)""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            persona_id INTEGER UNIQUE,
            FOREIGN KEY (persona_id) REFERENCES personas(id))""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS profesores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            persona_id INTEGER UNIQUE,
            departamento TEXT,
            FOREIGN KEY (persona_id) REFERENCES personas(id))""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS direccion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            persona_id INTEGER UNIQUE,
            cargo TEXT CHECK(cargo IN('Director', 'Jefe de Estudios', 'Secretario')),
            FOREIGN KEY (persona_id) REFERENCES personas(id))""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS aulas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT UNIQUE NOT NULL,
            capacidad INTEGER NOT NULL)""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS materiales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            aula_id INTEGER,
            FOREIGN KEY (aula_id) REFERENCES aulas(id))""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS asignaturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            departamento TEXT NOT NULL)""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            profesor_id INTEGER,
            aula_id INTEGER,
            asignatura_id INTEGER,
            anio_academico TEXT NOT NULL,
            FOREIGN KEY (profesor_id) REFERENCES profesores(id),
            FOREIGN KEY (aula_id) REFERENCES aulas(id),
            FOREIGN KEY (asignatura_id) REFERENCES asignaturas(id))""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL)""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS matriculas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alumno_id INTEGER NOT NULL,
                año_academico TEXT NOT NULL,
                UNIQUE(alumno_id, año_academico),
                FOREIGN KEY (alumno_id) REFERENCES alumnos(persona_id))""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS convocatorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE)""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS calificaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alumno_id INTEGER NOT NULL,
                asignatura_id INTEGER NOT NULL,
                convocatoria_id INTEGER NOT NULL,
                nota REAL NOT NULL CHECK(nota >= 0 AND nota <= 10),
                año_academico TEXT NOT NULL,
                UNIQUE(alumno_id, asignatura_id, convocatoria_id, año_academico),
                FOREIGN KEY (alumno_id) REFERENCES alumnos(persona_id),
                FOREIGN KEY (asignatura_id) REFERENCES asignaturas(id),
                FOREIGN KEY (convocatoria_id) REFERENCES convocatorias(id))""")

    #INSERT
        cursor.execute("""
                    INSERT OR IGNORE INTO usuarios (usuario, password) 
                    VALUES ('admin', '1234')""")
        # 1. Personas (Profe, Alumno y Director)
        cursor.execute(
            "INSERT OR IGNORE INTO personas (id, nombre, apellido, dni, telefono, email) VALUES (1, 'Ana', 'García', '12345678A', '600111222', 'ana@email.com')")
        cursor.execute(
            "INSERT OR IGNORE INTO personas (id, nombre, apellido, dni, telefono, email) VALUES (2, 'Luis', 'Pérez', '87654321B', '600333444', 'luis@email.com')")
        cursor.execute(
            "INSERT OR IGNORE INTO personas (id, nombre, apellido, dni, telefono, email) VALUES (3, 'Marta', 'Sánchez', '11223344C', '666777888', 'marta@email.com')")

        # 2. Asignar Roles (Alumnos, Profesores, Direccion)
        cursor.execute("INSERT OR IGNORE INTO profesores (id, persona_id, departamento) VALUES (1, 1, 'Informática')")
        cursor.execute("INSERT OR IGNORE INTO alumnos (id, persona_id) VALUES (1, 2)")
        cursor.execute("INSERT OR IGNORE INTO direccion (id, persona_id, cargo) VALUES (1, 3, 'Director')")

        # 3. Aulas
        cursor.execute("INSERT OR IGNORE INTO aulas (id, numero, capacidad) VALUES (1, '101', 30)")
        cursor.execute("INSERT OR IGNORE INTO aulas (id, numero, capacidad) VALUES (2, 'LAB-1', 15)")

        # 4. Asignaturas
        cursor.execute(
            "INSERT OR IGNORE INTO asignaturas (id, nombre, departamento) VALUES (1, 'Python', 'Informática')")
        cursor.execute("INSERT OR IGNORE INTO asignaturas (id, nombre, departamento) VALUES (2, 'SQL', 'Informática')")

        # 5. Materiales
        cursor.execute(
            "INSERT OR IGNORE INTO materiales (id, nombre, descripcion, aula_id) VALUES (1, 'Proyector', 'Epson 4K', 1)")

        # 6. Clases
        cursor.execute(
            "INSERT OR IGNORE INTO clases (id, profesor_id, aula_id, asignatura_id, anio_academico) VALUES (1, 1, 1, 1, '2025-2026')")

        # 7. Convocatorias (Importante para que Calificaciones no pete)
        cursor.execute("INSERT OR IGNORE INTO convocatorias (id, nombre) VALUES (1, 'Ordinaria')")
        cursor.execute("INSERT OR IGNORE INTO convocatorias (id, nombre) VALUES (2, 'Extraordinaria')")

        # 8. Matrículas (Luis en 2025-2026)
        cursor.execute("INSERT OR IGNORE INTO matriculas (id, alumno_id, año_academico) VALUES (1, 2, '2025-2026')")

        # 9. Calificaciones (Nota para Luis en Python)
        cursor.execute(
            "INSERT OR IGNORE INTO calificaciones (alumno_id, asignatura_id, convocatoria_id, nota, año_academico) VALUES (2, 1, 1, 8.5, '2025-2026')")

        connection.commit()  # Aseguramos que se guardan los cambios