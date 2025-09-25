def log_entero(n, base):
    resultado = 0
    while n >= base:
        n //= base
        resultado += 1
    return resultado
