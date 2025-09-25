def secuencia(numero):
    if numero == 1:
        return 2
    else:
        return secuencia(numero-1) + (2*numero)
