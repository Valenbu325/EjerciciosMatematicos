from view.menu import pedir_opcion, mostrar_menu
from controller.controller import ejecutar_ejercicio


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        if opcion == "0":
            print("Saliendo...")
            break
        else:
            ejecutar_ejercicio(opcion)
