from inventario import Inventario

def main():
    inv = Inventario()

    while True:
        print("\n==== Menú Principal ====")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Mostrar todos los productos")
        print("4. Salir")
        op = input("Elige una opción: ")

        if op == "1":
            inv.agregar_producto()
        elif op == "2":
            inv.buscar_producto()
        elif op == "3":
            inv.mostrar_productos()
        elif op == "4":
            inv.cerrar()
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()
