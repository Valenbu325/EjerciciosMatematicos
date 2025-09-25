def sucesion_especial(numero: int) -> float:
        """Función recursiva de la sucesión."""
        if numero == 1:
            return 2
        elif numero >= 2:
            return numero + 1 / sucesion_especial(numero - 1)
        else:
            raise ValueError("numero debe ser un entero positivo.")
