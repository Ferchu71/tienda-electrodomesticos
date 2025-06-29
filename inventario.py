from producto import Producto
from cliente import Cliente
from db_manager import DBManager

class Inventario:
    def __init__(self):
        self.db = DBManager()

    # --- PRODUCTOS ---

    def agregar_producto(self):
        print("\n--- Agregar Producto ---")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        producto = Producto(nombre, categoria, precio, stock)
        self.db.agregar_producto(producto)
        print("✅ Producto agregado.\n")

    def buscar_producto(self):
        nombre = input("🔎 Buscar producto por nombre: ")
        resultados = self.db.buscar_producto_por_nombre(nombre)
        if resultados:
            for p in resultados:
                print(f"ID: {p[0]} | {p[1]} | {p[2]} | ${p[3]} | Stock: {p[4]}")
        else:
            print("❌ Producto no encontrado.")

    def mostrar_productos(self):
        print("\n📦 Lista de productos:")
        productos = self.db.obtener_todos_los_productos()
        for p in productos:
            print(f"ID: {p[0]} | {p[1]} | {p[2]} | ${p[3]} | Stock: {p[4]}")
        print()

    # --- CLIENTES ---

    def registrar_cliente(self):
        print("\n--- Registrar Cliente ---")
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        telefono = input("Teléfono: ")
        cliente = Cliente(nombre, dni, telefono)
        self.db.agregar_cliente(cliente)
        print("✅ Cliente registrado.\n")

    def mostrar_clientes(self):
        print("\n👥 Lista de clientes:")
        clientes = self.db.obtener_todos_los_clientes()
        for c in clientes:
            print(f"ID: {c[0]} | {c[1]} | DNI: {c[2]} | Tel: {c[3]}")
        print()

    # --- VENTAS ---

    def realizar_venta(self):
        print("\n🛒 --- Realizar Venta ---")
        dni = input("DNI del cliente: ")
        cliente = self.db.obtener_cliente_por_dni(dni)
        if not cliente:
            print("❌ Cliente no encontrado. Registralo primero.")
            return

        cliente_id = cliente[0]
        items = []
        while True:
            producto_id = int(input("ID del producto a vender: "))
            cantidad = int(input("Cantidad: "))
            producto = next((p for p in self.db.obtener_todos_los_productos() if p[0] == producto_id), None)
            if not producto:
                print("❌ Producto no encontrado.")
                continue
            if cantidad > producto[4]:
                print("⚠️ Stock insuficiente.")
                continue
            items.append((producto_id, cantidad, producto[3]))

            otro = input("¿Agregar otro producto? (s/n): ").lower()
            if otro != "s":
                break

        venta_id = self.db.registrar_venta(cliente_id, items)
        print(f"✅ Venta registrada con ID: {venta_id}")

    def mostrar_ventas(self):
        print("\n📈 Historial de ventas:")
        ventas = self.db.obtener_ventas()
        for v in ventas:
            print(f"\n🧾 Venta ID: {v[0]} | Cliente: {v[1]} | Fecha: {v[2]}")
            detalles = self.db.obtener_detalle_venta(v[0])
            for d in detalles:
                print(f"  - Producto: {d[0]} | Cantidad: {d[1]} | Precio: ${d[2]}")
        print()

    def cerrar(self):
        self.db.cerrar()

