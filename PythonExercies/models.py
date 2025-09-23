# models.py
# Sólo las funciones tal como las hiciste tú

def suma(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma(numero-1)


def invertir_texto(texto):
    texto_invertido = texto[::-1]
    return texto_invertido


def serie_armonica(numero):
    if numero == 1:
        return 1
    else:
        return 1/numero + serie_armonica(numero-1)


def secuencia(numero):
    if numero == 1:
        return 2
    else:
        return secuencia(numero-1) + (2*numero)


# stub para los no implementados
def not_implemented_stub(*args, **kwargs):
    raise NotImplementedError("Este ejercicio no está implementado aún.")
