def mostrar_menu():
    print("\n=== MENÚ DE EJERCICIOS ===")
    print("1. Fibonacci")
    print("2. Suma de números")
    print("6. Invertir texto")
    print("7. Serie armónica")
    print("9. Logaritmo entero")
    print("10. Contar dígitos")
    print("19. sucesión especial")
#   print("24. ")
    print("28. secuencia")
    print("0. Salir")

def pedir_opcion():
    return input("Elige una opción: ")

def pedir_entero(mensaje="Introduce un número: "):
    return int(input(mensaje))

def pedir_texto(mensaje="Introduce un texto: "):
    return input(mensaje)

def mostrar_resultado(resultado):
    print("Resultado:", resultado)
