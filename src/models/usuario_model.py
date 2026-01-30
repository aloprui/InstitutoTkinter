from database.quieries import get_connection

class UsuarioModel:

    @staticmethod
    def crear(usuario, password):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios(usuario, password) VALUES (?, ?)",(usuario, password))
            conn.commit()

    @staticmethod
    def verificar(usuario, password):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM usuarios WHERE usuario = ? AND password = ?",
                (usuario, password)
            )
            return cursor.fetchone()