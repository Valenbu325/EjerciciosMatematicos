class Ejercicio19View:
    def pedir_numero(self) -> int:
        return int(input("Ingrese un número entero positivo: "))

    def mostrar_resultado(self, n: int, resultado: float):
        print(f"f({n}) = {resultado}")
