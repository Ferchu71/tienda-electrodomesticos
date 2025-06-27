import sqlite3

class DBManager:
    def __init__(self, db_name="productos.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._crear_tabla()

    def _crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT,
                precio REAL,
                stock INTEGER
            )
        """)
        self.conn.commit()

    def agregar_producto(self, producto):
        self.cursor.execute(
            "INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)",
            (producto.nombre, producto.categoria, producto.precio, producto.stock)
        )
        self.conn.commit()

    def buscar_por_nombre(self, nombre):
        self.cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
        return self.cursor.fetchall()

    def obtener_todos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def cerrar(self):
        self.conn.close()
