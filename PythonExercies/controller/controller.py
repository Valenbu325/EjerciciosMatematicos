# controller.py
# Controlador mínimo que conecta vista y modelo

from models import (
    suma,
    invertir_texto,
    serie_armonica,
    secuencia,
    not_implemented_stub,
)
import view

# Sólo estos numerales están implementados (tal como pediste)
IMPLEMENTED = {2, 6, 7, 28}


def ejecutar_ejercicio(numero: int):
    try:
        if numero == 2:
            numero_usuario = views.pedir_entero("Ingrese el numero que desea sumar: ")
            resultado = suma(numero_usuario)
            views.mostrar_resultado(f"La suma es: {resultado}")

        elif numero == 6:
            texto = views.pedir_cadena("Ingrese el texto que desea invertir: ")
            resultado = invertir_texto(texto)
            views.mostrar_resultado(resultado)

        elif numero == 7:
            numero_usuario = views.pedir_entero("Ingrese el numero hasta el cual desea la serie armonica: ")
            resultado = serie_armonica(numero_usuario)
            views.mostrar_resultado(f"El resultado de la suma de la serie armonica es: {resultado}")

        elif numero == 28:
            numero_usuario = views.pedir_entero("Ingrese el numero de la secuencia: ")
            resultado = secuencia(numero_usuario)
            views.mostrar_resultado(f"La secuencia es: {resultado}")

        else:
            views.mostrar_resultado(f"El ejercicio {numero} no está implementado aún. (Agrega la función en models.py)")
    except Exception as e:
        views.mostrar_error(str(e))


from models.Ejercicio9 import log_entero
    def run(views):
    try:
        n, b = views.pedir_datos()
        resultado = log_entero(n, b)
        views.mostrar_resultado(n, b, resultado)
    except Exception as e:
        view.mostrar_error(str(e))
