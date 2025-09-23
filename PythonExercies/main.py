# main.py
# Punto de entrada mínimo

from controller import ejecutar_ejercicio, IMPLEMENTED
import views

def main():
    while True:
        views.mostrar_menu(IMPLEMENTED)
        opcion = views.pedir_entero("Selecciona el número del ejercicio (0 para salir): ", min_val=0, max_val=31)
        if opcion == 0:
            print("Adiós.")
            break
        ejecutar_ejercicio(opcion)

if __name__ == "__main__":
    main()
