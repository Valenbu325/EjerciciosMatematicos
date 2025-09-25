from view.menu import menu, pedir_numero, mostrar_resultado
from controller.controller import ejecutar_suma

if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == "1":
            n = pedir_numero()
            resultado = ejecutar_suma(n)
            mostrar_resultado(resultado)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")