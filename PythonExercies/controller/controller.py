# controller.py
# Controlador mínimo que conecta vista y modelo
from models.Ejercicio1 import fibonacci
from models.Ejercicio2 import suma
from models.Ejercicio6 import invertir_texto
from models.Ejercicio7 import serie_armonica
from models.Ejercicio9 import logaritmo_entero
from models.Ejercicio10 import contar_digitos
from models.Ejercicio19 import sucesion_especial
#from models.Ejercicio24 import funcion_24
from models.Ejercicio28 import secuencia

import view.menu as menu

def ejecutar_ejercicio(opcion: str):
    try:
        if opcion == "1":
            numero_usuario = menu.pedir_entero("Ingrese el numero de la serie Fibonacci que desea: ")
            resultado = fibonacci(numero_usuario)
            menu.mostrar_resultado(f"El numero de la serie Fibonacci es: {resultado}")
        
        elif opcion == "2":
            numero_usuario = menu.pedir_entero("Ingrese el numero que desea sumar: ")
            resultado = suma(numero_usuario)
            menu.mostrar_resultado(f"La suma es: {resultado}")
            
        elif opcion == "6":
            texto = menu.pedir_texto("Ingrese el texto que desea invertir: ")
            resultado = invertir_texto(texto)
            menu.mostrar_resultado(resultado)
            
        elif opcion == "7":
            numero_usuario = menu.pedir_entero("Ingrese el numero hasta el cual desea la serie armonica: ")
            resultado = serie_armonica(numero_usuario)
            menu.mostrar_resultado(f"El resultado de la suma de la serie armonica es: {resultado}")
        
        elif opcion == "9":
            numero_usuario = menu.pedir_entero("Ingrese el numero: ")
            base_usuario = menu.pedir_entero("Ingrese la base: ")
            resultado = logaritmo_entero(numero_usuario, base_usuario)
            menu.mostrar_resultado(f"El logaritmo entero es: {resultado}")
        
        elif opcion == "10":
            numero_usuario = menu.pedir_entero("Ingrese el numero: ")
            resultado = contar_digitos(numero_usuario)
            menu.mostrar_resultado(f"El numero de digitos es: {resultado}")
        
        elif opcion == "19":
            numero_usuario = menu.pedir_entero("Ingrese el numero de la sucesión: ")
            resultado = sucesion_especial(numero_usuario)
            menu.mostrar_resultado(f"El resultado de la sucesión es: {resultado}")
            
#        elif opcion == "24":
#            numero_usuario = menu.pedir_entero("Ingrese el numero: ")
#            resultado = funcion_24(numero_usuario)

        elif opcion == "28":
            numero_usuario = menu.pedir_entero("Ingrese el numero de la secuencia: ")
            resultado = secuencia(numero_usuario)
            menu.mostrar_resultado(f"La secuencia es: {resultado}")
        
        else:
            menu.mostrar_resultado(f"El ejercicio {opcion} no está implementado aún. (Agrega la función en models.py)")
            
    except Exception as e:
        menu.mostrar_resultado(str(e))
        
# Lista de ejercicios implementados
IMPLEMENTED = ["1", "2", "3", "4", "5", "6", "7", "9"])
