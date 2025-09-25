from view.menu import mostrar_menu, pedir_opcion
from controller.controller import ejecutar_ejercicio

if __name__ == "__main__":  
    print("🔢 Bienvenido a los Ejercicios Matemáticos")
    
    while True:
        try:
            mostrar_menu()
            opcion = pedir_opcion()
            
            if opcion == "0":
                print("¡Hasta luego! 👋")
                break
            else:
                ejecutar_ejercicio(opcion)
                # Pausa para que el usuario vea el resultado
                input("\nPresiona Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("El programa continuará...")
