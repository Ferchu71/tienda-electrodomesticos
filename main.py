from inventario import Inventario

def main():
    sistema = Inventario()

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Mostrar productos")
        print("4. Registrar cliente")
        print("5. Mostrar clientes")
        print("6. Realizar venta")
        print("7. Ver historial de ventas")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.agregar_producto()
        elif opcion == "2":
            sistema.buscar_producto()
        elif opcion == "3":
            sistema.mostrar_productos()
        elif opcion == "4":
            sistema.registrar_cliente()
        elif opcion == "5":
            sistema.mostrar_clientes()
        elif opcion == "6":
            sistema.realizar_venta()
        elif opcion == "7":
            sistema.mostrar_ventas()
        elif opcion == "8":
            sistema.cerrar()
            print("👋 Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()