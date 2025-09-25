def serie_armonica(numero):
    if numero == 1:
        return 1
    else:
        return 1/numero + serie_armonica(numero-1)
