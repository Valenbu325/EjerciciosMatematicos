def contar_digitos(numero):
    numero = abs(numero)
    if numero < 10: return 1
    return 1 + contar_digitos(numero//10)
