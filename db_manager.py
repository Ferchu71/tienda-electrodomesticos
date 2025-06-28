import pyodbc
from producto import Producto

class DBManager:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=PC_Estudio\\SQLEXPRESS;"
                "DATABASE=TiendaElectrodomesticos;"
                "Trusted_Connection=yes;"
            )
            self.cursor = self.conn.cursor()
            print("✅ Conexión a SQL Server establecida.")
        except Exception as e:
            print(f"❌ Error de conexión: {e}")

    def agregar_producto(self, producto: Producto):
        try:
            self.cursor.execute("""
                INSERT INTO Productos (Nombre, Categoria, Precio, Stock)
                VALUES (?, ?, ?, ?)
            """, (producto.nombre, producto.categoria, producto.precio, producto.stock))
            self.conn.commit()
            print("✅ Producto agregado correctamente.")
        except Exception as e:
            print(f"❌ Error al agregar producto: {e}")

    def buscar_por_nombre(self, nombre):
        try:
            self.cursor.execute("""
                SELECT * FROM Productos
                WHERE Nombre LIKE ?
            """, ('%' + nombre + '%',))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"❌ Error en búsqueda: {e}")
            return []

    def obtener_todos(self):
        try:
            self.cursor.execute("SELECT * FROM Productos")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"❌ Error al obtener productos: {e}")
            return []

    def cerrar(self):
        self.conn.close()

