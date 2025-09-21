# Árbol de Sintaxis con Python y NetworkX

Este proyecto implementa un parser recursivo descendente que construye y dibuja el árbol de sintaxis a partir de una gramática libre de contexto definida en un archivo (`gra.txt`).

Se utiliza [`networkx`](https://networkx.org/) para manejar el grafo y [`matplotlib`](https://matplotlib.org/) para visualizarlo.

---

## Requisitos

- Python 3.10+ (en macOS se recomienda instalarlo con [Homebrew](https://brew.sh/)):
  
    ```bash
    brew install python

## Entorno virtual:
- Crear y entrar en el entorno:

    ```bash
    python3 -m venv venv
    source venv/bin/activate

- Instalar dependencias necesarias (networkx y matplotlib):

    ```bash
    pip install networkx matplotlib

## Uso

- Ejecutar el programa:
    ```bash
    python arbol.py

- Ingresar una cadena para probar (ejemplo):

    ```bash
    Ingrese una cadena (o 'salir'): 2 + 3 * 4
    Cadena aceptada

Se abrirá una ventana con el árbol de sintaxis.

## Notas

- La gramática se define en gra.txt.

- El símbolo ε representa una producción vacía (epsilon).

- Cualquier número entero ingresado se interpreta como num.
