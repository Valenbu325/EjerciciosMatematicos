from view.menu import mostrar_menu, pedir_opcion, pedir_entero, pedir_texto, mostrar_resultado

# Importamos todos los modelos
from models.Ejercicio1 import fibonacci
from models.Ejercicio2 import suma
from models.Ejercicio6 import invertir_texto
from models.Ejercicio7 import serie_armonica
from models.Ejercicio9 import log_entero
from models.Ejercicio10 import contar_digitos
from models.Ejercicio19 import Sucesion 
from models.Ejercicio28 import secuencia


def ejecutar():
    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "1":
            n = pedir_entero("Introduce n: ")
            mostrar_resultado(fibonacci(n))

        elif opcion == "2":
            n = pedir_entero("Introduce un número: ")
            mostrar_resultado(suma(n))

        elif opcion == "3":
            texto = pedir_texto("Introduce un texto: ")
            mostrar_resultado(invertir_texto(texto))

        elif opcion == "4":
            n = pedir_entero("Introduce n: ")
            mostrar_resultado(serie_armonica(n))

        elif opcion == "5":
            n = pedir_entero("Introduce número: ")
            base = pedir_entero("Introduce base: ")
            mostrar_resultado(log_entero(n, base))

        elif opcion == "6":
            n = pedir_entero("Introduce número: ")
            mostrar_resultado(contar_digitos(n))

        elif opcion == "7":
            n = pedir_entero("Introduce n: ")
            mostrar_resultado(Sucesion().f(n))

        elif opcion == "8":
            n = pedir_entero("Introduce número: ")
            mostrar_resultado(secuencia(n))

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")
