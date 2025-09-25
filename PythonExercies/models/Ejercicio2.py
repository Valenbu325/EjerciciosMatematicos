def suma(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma(numero-1)