from controller.ejercicio19_controller import Ejercicio19Controller
from view.ejercicio19_view import Ejercicio19View
from model.ejercicio19_model import Ejercicio19Model

from controller.ejercicio9_controller import run as ejercicio9_run
from view import ejercicio9_view

def ejercicio2():
    def suma(numero):
        if numero == 0:
            return 0
        else:
            return numero + suma(numero-1)
    numero_usuario = int(input("Ingrese el número que desea sumar: "))
    print("La suma es:", suma(numero_usuario))

def ejercicio6():
    texto = input('Ingrese el texto que desea invertir: ')
    texto_invertido = texto[::-1]
    print("Texto invertido:", texto_invertido)

def ejercicio7():
    def serie_armonica(numero):
        if numero == 1:
            return 1
        else: 
            return 1/numero + serie_armonica(numero-1)
    numero_usuario = int(input('Ingrese el número hasta el cual desea la serie armónica: '))
    print('El resultado de la suma de la serie armónica es:', serie_armonica(numero_usuario))

def ejercicio10():
    def secuencia(numero):
        if numero == 1:
            return 2
        else:
            return secuencia(numero-1) + (2*numero)
    numero_usuario = int(input('Ingrese el número de la secuencia: '))
    print('La secuencia es:', secuencia(numero_usuario))

def mostrar_menu():
    print("\n=== MENÚ DE EJERCICIOS ===")
    print("1. Ejercicio 9 - Logaritmo entero")
    print("2. Ejercicio 19 - Sucesión recursiva")
    print("3. Ejercicio 2 - Suma recursiva")
    print("4. Ejercicio 6 - Invertir texto")
    print("5. Ejercicio 7 - Serie armónica")
    print("6. Ejercicio 10 - Secuencia")
    print("0. Salir")

# --- MAIN ---
if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ejercicio9_run(ejercicio9_view)
        elif opcion == "2":
            view = Ejercicio19View()
            model = Ejercicio19Model()
            controller = Ejercicio19Controller(model, view)
            controller.ejecutar()
        elif opcion == "3":
            ejercicio2()
        elif opcion == "4":
            ejercicio6()
        elif opcion == "5":
            ejercicio7()
        elif opcion == "6":
            ejercicio10()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")