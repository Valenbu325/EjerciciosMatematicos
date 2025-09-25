# models.py
# Sólo las funciones tal como las hiciste tú







def secuencia(numero):
    if numero == 1:
        return 2
    else:
        return secuencia(numero-1) + (2*numero)


# stub para los no implementados
def not_implemented_stub(*args, **kwargs):
    raise NotImplementedError("Este ejercicio no está implementado aún.")
