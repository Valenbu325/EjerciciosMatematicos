def logaritmo_entero(numero, base):
    resultado = 0
    while numero >= base:
        numero //= base
        resultado += 1
    return resultado

