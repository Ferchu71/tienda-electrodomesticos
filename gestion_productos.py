import sqlite3

# Crear o conectar a la base de datos
conn = sqlite3.connect("productos.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT,
        precio REAL,
        stock INTEGER
    )
""")
conn.commit()

# Función para agregar producto
def agregar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    cursor.execute("INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)",
                   (nombre, categoria, precio, stock))
    conn.commit()
    print("✅ Producto agregado correctamente.\n")

# Función para buscar producto por nombre
def buscar_producto():
    nombre = input("🔎 Ingrese nombre o parte del nombre a buscar: ")
    cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = cursor.fetchall()

    if resultados:
        print("\n📋 Resultados encontrados:")
        for prod in resultados:
            print(f"ID: {prod[0]}, Nombre: {prod[1]}, Categoría: {prod[2]}, Precio: ${prod[3]}, Stock: {prod[4]}")
    else:
        print("❌ No se encontraron productos con ese nombre.\n")

# Función para mostrar todos los productos
def mostrar_todos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    print("\n📦 Inventario completo:")
    for prod in productos:
        print(f"ID: {prod[0]}, Nombre: {prod[1]}, Categoría: {prod[2]}, Precio: ${prod[3]}, Stock: {prod[4]}")

# Menú principal
def menu():
    while True:
        print("\n====== TIENDA DE ELECTRODOMÉSTICOS ======")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Mostrar todos los productos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            mostrar_todos()
        elif opcion == "4":
            print("👋 Saliendo del programa.")
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

# Ejecutar programa
if __name__ == "__main__":
    menu()
    conn.close()
