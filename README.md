# Proyecto Python - Patrón Modelo-Vista-Controlador (MVC)



## Descripción

Este proyecto consiste en desarrollar una aplicación en **Python** que implemente el patrón de arquitectura **Modelo-Vista-Controlador (MVC)**. El objetivo es estructurar el código de manera que se separen claramente las responsabilidades de acceso a datos (Modelo), la presentación visual (Vista) y la lógica de control (Controlador).

El programa principal debe mostrar un menú interactivo que permita al usuario seleccionar y resolver una serie de ejercicios matemáticos. El menú debe incluir los ejercicios numerados **7, 9, 19, 24 y 28**, y el grupo deberá seleccionar otros **cinco ejercicios** adicionales para completar un total de **10 ejercicios** de los 31 planteados.

## Estructura del proyecto

La estructura recomendada para implementar el patrón MVC es la siguiente:

```
ProyectoMVC/
│
├── modelos/            # Clases y funciones que representan la lógica de negocio y datos
│   ├── ejercicio7.py
│   ├── ejercicio9.py
│   ├── ejercicio19.py
│   ├── ejercicio24.py
│   ├── ejercicio28.py
│   └── ejercicioX.py   # Otros ejercicios seleccionados
│
├── vistas/             # Interfaces de usuario, mensajes y salida visual
│   ├── menu.py
│   ├── vista_ejercicio7.py
│   └── ...
│
├── controladores/      # Lógica de interacción entre modelo y vista
│   ├── controlador_ejercicio7.py
│   └── ...
│
├── main.py             # Punto de entrada de la aplicación
│
└── README.md           # Documentación del proyecto
```

## Requisitos

- **Python 3.7+**
- Uso claro del patrón Modelo-Vista-Controlador
- Menú interactivo para la selección de ejercicios
- Implementación de los ejercicios 7, 9, 19, 24, 28 y cinco más a elección del grupo
- Código bien comentado y organizado

## Ejercicios incluidos

1. **Ejercicio 7**  
2. **Ejercicio 9**  
3. **Ejercicio 19**  
4. **Ejercicio 24**  
5. **Ejercicio 28**  
6. **Ejercicio X** (selección del grupo)
7. **Ejercicio Y** (selección del grupo)
8. **Ejercicio Z** (selección del grupo)
9. **Ejercicio W** (selección del grupo)
10. **Ejercicio V** (selección del grupo)

> **Nota:** Actualiza los nombres de los ejercicios seleccionados por el grupo y describe brevemente cada uno en este apartado.

## ¿Cómo ejecutar el proyecto?

1. Clona el repositorio:
    ```bash
    git clone https://github.com/usuario/ProyectoMVC.git
    cd ProyectoMVC
    ```

2. Instala los requisitos (si existen):
    ```bash
    pip install -r requirements.txt
    ```

3. Ejecuta el archivo principal:
    ```bash
    python main.py
    ```

4. Sigue las instrucciones en pantalla para seleccionar y resolver los ejercicios.

## Ejemplo de uso

Al iniciar el programa, se mostrará un menú con los ejercicios disponibles. El usuario podrá seleccionar el número correspondiente y resolver el ejercicio propuesto.

```
==============================
   Menú de Ejercicios MVC
==============================
1. Ejercicio 7
2. Ejercicio 9
3. Ejercicio 19
4. Ejercicio 24
5. Ejercicio 28
6. Ejercicio X
7. Ejercicio Y
8. Ejercicio Z
9. Ejercicio W
10. Ejercicio V
0. Salir
Seleccione una opción:
```

## Detalles sobre la arquitectura MVC

- **Modelo:** Contiene la lógica de los ejercicios matemáticos. Cada ejercicio está implementado como una clase o función independiente dentro de la carpeta `modelos`.
- **Vista:** Gestiona la presentación y la interacción con el usuario. Los mensajes, menús y resultados se encuentran en la carpeta `vistas`.
- **Controlador:** Coordina la interacción entre el modelo y la vista, gestionando el flujo según las acciones del usuario. Los controladores se encuentran en la carpeta `controladores`.

## Contribuciones

Si deseas mejorar el proyecto, puedes realizar un fork y enviar un pull request. No olvides comentar el código y seguir la estructura MVC propuesta.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autores

- Andres Moreno
- Valentina Burgos
- Luis Agudelo
- Aron Agudelo

---

> **Referencia de la consigna:**  
> Desarrollar un proyecto en Python que implemente el patrón de arquitectura Modelo-Vista-Controlador (MVC). El proyecto deberá incluir un menú que presente los ejercicios numerales 7, 9, 19, 24, 28 y el grupo debe seleccionar cinco ejercicios más para un total de 10 de los 31 ejercicios planteados.
