from model.ejercicio9_model import log_entero

def run(view):
    try:
        n, b = view.pedir_datos()
        resultado = log_entero(n, b)
        view.mostrar_resultado(n, b, resultado)
    except Exception as e:
        view.mostrar_error(str(e))
