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