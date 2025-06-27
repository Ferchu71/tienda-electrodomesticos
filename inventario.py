from producto import Producto
from db_manager import DBManager

class Inventario:
    def __init__(self):
        self.db = DBManager()

    def agregar_producto(self):
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        prod = Producto(nombre, categoria, precio, stock)
        self.db.agregar_producto(prod)
        print("✅ Producto agregado con éxito.")

    def buscar_producto(self):
        nombre = input("🔎 Buscar nombre: ")
        resultados = self.db.buscar_por_nombre(nombre)
        if resultados:
            for r in resultados:
                print(f"ID: {r[0]}, {r[1]} | {r[2]} | ${r[3]} | Stock: {r[4]}")
        else:
            print("❌ No encontrado.")

    def mostrar_productos(self):
        productos = self.db.obtener_todos()
        print("\n📦 Inventario:")
        for p in productos:
            print(f"ID: {p[0]}, {p[1]} | {p[2]} | ${p[3]} | Stock: {p[4]}")

    def cerrar(self):
        self.db.cerrar()
