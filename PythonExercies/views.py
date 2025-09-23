# views.py
# Vista simple para entrada/salida

def mostrar_menu(implemented_set):
    print("\n=== MENÚ: Ejercicios (1..31) ===")
    for i in range(1, 32):
        mark = "*" if i in implemented_set else " "
        print(f"{i:2d}. Ejercicio {i:2d} {mark}")
    print("\n* = implementado")
    print("0. Salir\n")


def pedir_entero(prompt: str, min_val=None, max_val=None) -> int:
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Ingrese un número >= {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"Ingrese un número <= {max_val}.")
                continue
            return val
        except ValueError:
            print("Entrada no válida. Intente de nuevo con un entero.")


def pedir_cadena(prompt: str) -> str:
    return input(prompt)


def mostrar_resultado(msg: str):
    print("\n--- Resultado ---")
    print(msg)
    print("-----------------\n")


def mostrar_error(msg: str):
    print(f"\n[ERROR] {msg}\n")
