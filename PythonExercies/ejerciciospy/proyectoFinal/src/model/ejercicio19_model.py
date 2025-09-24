class Ejercicio19Model:
    def f(self, n: int) -> float:
        """Función recursiva de la sucesión."""
        if n == 1:
            return 2
        elif n >= 2:
            return n + 1 / self.f(n - 1)
        else:
            raise ValueError("n debe ser un entero positivo.")