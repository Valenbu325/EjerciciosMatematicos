class MenuController:
    def __init__(self, view: MenuView):
        self.view = view

    def ejecutar(self):
        while True:
            self.view.mostrar_menu()
            opcion = self.view.pedir_opcion()

            if opcion == 1:
                model = Ejercicio19Model()
                view = Ejercicio19View()
                controller = Ejercicio19Controller(model, view)
                controller.ejecutar()

            elif opcion == 0:
                print("Saliendo... 👋")
                break

            else:
                print("Opción inválida, intente de nuevo.")