def pedir_datos():
    n = int(input("Introduce el número n (n >= 1): "))
    b = int(input("Introduce la base b (b > 1): "))
    return n, b

def mostrar_resultado(n, b, resultado):
    print(f"El logaritmo entero de {n} en base {b} es: {resultado}")

def mostrar_error(mensaje):
    print(f"Error: {mensaje}")