from model.ejercicio19_model import Ejercicio19Model
from view.ejercicio19_view import Ejercicio19View

class Ejercicio19Controller:
    def __init__(self, model: Ejercicio19Model, view: Ejercicio19View):
        self.model = model
        self.view = view

    def ejecutar(self):
        n = self.view.pedir_numero()
        resultado = self.model.f(n)
        self.view.mostrar_resultado(n, resultado)