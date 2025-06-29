import pyodbc
from producto import Producto
from cliente import Cliente

class DBManager:
    def __init__(self, servidor='PC_ESTUDIO\\SQLEXPRESS', base_datos='tienda_electrodomesticosDB'):
        self.conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={servidor};"
            f"DATABASE={base_datos};"
            f"Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()

    # --- PRODUCTOS ---

    def agregar_producto(self, producto):
        self.cursor.execute(
            "INSERT INTO Productos (Nombre, Categoria, Precio, Stock) VALUES (?, ?, ?, ?)",
            (producto.nombre, producto.categoria, producto.precio, producto.stock)
        )
        self.conn.commit()

    def buscar_producto_por_nombre(self, nombre):
        self.cursor.execute("SELECT * FROM Productos WHERE Nombre LIKE ?", ('%' + nombre + '%',))
        return self.cursor.fetchall()

    def obtener_todos_los_productos(self):
        self.cursor.execute("SELECT * FROM Productos")
        return self.cursor.fetchall()

    def actualizar_stock(self, producto_id, cantidad):
        self.cursor.execute("""
            UPDATE Productos
            SET Stock = Stock - ?
            WHERE Id = ?
        """, (cantidad, producto_id))
        self.conn.commit()

    # --- CLIENTES ---

    def agregar_cliente(self, cliente):
        self.cursor.execute(
            "INSERT INTO Clientes (Nombre, DNI, Telefono) VALUES (?, ?, ?)",
            (cliente.nombre, cliente.dni, cliente.telefono)
        )
        self.conn.commit()

    def obtener_cliente_por_dni(self, dni):
        self.cursor.execute("SELECT * FROM Clientes WHERE DNI = ?", (dni,))
        return self.cursor.fetchone()

    def obtener_todos_los_clientes(self):
        self.cursor.execute("SELECT * FROM Clientes")
        return self.cursor.fetchall()

    # --- VENTAS ---

    def registrar_venta(self, cliente_id, items):
        """
        items: lista de tuplas (producto_id, cantidad, precio_unitario)
        """
        # Registrar venta
        self.cursor.execute("INSERT INTO Ventas (ClienteId) VALUES (?)", (cliente_id,))
        self.conn.commit()

        venta_id = self.cursor.execute("SELECT SCOPE_IDENTITY()").fetchval()

        for producto_id, cantidad, precio_unitario in items:
            # Insertar detalle de venta
            self.cursor.execute("""
                INSERT INTO DetalleVentas (VentaId, ProductoId, Cantidad, PrecioUnitario)
                VALUES (?, ?, ?, ?)
            """, (venta_id, producto_id, cantidad, precio_unitario))

            # Actualizar stock
            self.actualizar_stock(producto_id, cantidad)

        self.conn.commit()
        return venta_id

    def obtener_ventas(self):
        self.cursor.execute("""
            SELECT V.Id, C.Nombre, V.Fecha
            FROM Ventas V
            JOIN Clientes C ON V.ClienteId = C.Id
            ORDER BY V.Fecha DESC
        """)
        return self.cursor.fetchall()

    def obtener_detalle_venta(self, venta_id):
        self.cursor.execute("""
            SELECT P.Nombre, D.Cantidad, D.PrecioUnitario
            FROM DetalleVentas D
            JOIN Productos P ON D.ProductoId = P.Id
            WHERE D.VentaId = ?
        """, (venta_id,))
        return self.cursor.fetchall()

    # --- CIERRE ---

    def cerrar(self):
        self.conn.close()

