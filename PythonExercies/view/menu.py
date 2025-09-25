def mostrar_menu():
    print("\n=== MENÚ DE EJERCICIOS ===")
    print("1. Fibonacci")
    print("2. Suma de números")
    print("3. Invertir texto")
    print("4. Serie armónica")
    print("5. Logaritmo entero")
    print("6. Contar dígitos")
    print("7. sucesión especial")
    print("8. ")
    print("9. secuencia")
    print("0. Salir")

def pedir_opcion():
    return input("Elige una opción: ")

def pedir_entero(mensaje="Introduce un número: "):
    return int(input(mensaje))

def pedir_texto(mensaje="Introduce un texto: "):
    return input(mensaje)

def mostrar_resultado(resultado):
    print("Resultado:", resultado)
