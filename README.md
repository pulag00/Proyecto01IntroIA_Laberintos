# Proyecto01IntroIA_Laberintos

## Descripción
Este proyecto implementa un programa en Python capaz de encontrar la solución de un laberinto representado como una matriz NxN, aplicando tres algoritmos de búsqueda:

- **DFS** — Búsqueda primero en profundidad *(búsqueda ciega)*
- **BFS** — Búsqueda primero en anchura *(búsqueda ciega)*
- **A\*** — A estrella con heurística Manhattan *(búsqueda heurística)*

Para cada algoritmo se visualiza tanto el grafo como la matriz coloreada con las celdas exploradas y el camino final encontrado.

---

## Estructura del Proyecto

```
Proyecto01IntroIA_Laberintos/
│
├── main.py            # Punto de entrada: define el laberinto y ejecuta los algoritmos
├── maze.py            # Clase Maze: encapsula la matriz del laberinto
├── graph.py           # Clase Graph y conversión de matriz a grafo de adyacencia
├── heuristics.py      # Función heurística Manhattan y construcción de la tabla h(n)
├── search.py          # Implementación de DFS, BFS y A*
├── utils.py           # Utilidad para reconstruir el camino desde el diccionario de padres
├── visualization.py   # Visualización del grafo y la matriz con matplotlib/networkx
└── README.md
```

---

## Representación del Laberinto

El laberinto se define como una matriz NxN con la siguiente convención:

| Valor | Significado            |
|-------|------------------------|
| `0`   | Espacio libre          |
| `1`   | Pared (no transitable) |
| `2`   | Celda de inicio        |
| `3`   | Celda meta             |

---

## Algoritmos Implementados

### 1. DFS — Depth First Search
Explora el grafo siguiendo un camino hasta el fondo antes de retroceder. Usa una **pila (LIFO)**. No garantiza el camino más corto, pero puede ser más eficiente en memoria para laberintos con soluciones profundas.

### 2. BFS — Breadth First Search
Explora todos los nodos nivel por nivel usando una **cola (FIFO)**. Garantiza encontrar el **camino más corto** cuando todos los costos son iguales (peso uniforme de 1).

### 3. A\* — A Estrella
Combina el costo real acumulado `g(n)` con una estimación heurística `h(n)` para guiar la búsqueda hacia la meta de forma eficiente:

```
f(n) = g(n) + h(n)
```

La heurística utilizada es la **distancia Manhattan**:

```
h(n) = |fila_n - fila_meta| + |col_n - col_meta|
```

Esta heurística es **admisible** (nunca sobreestima), lo que garantiza que A\* encuentre el camino óptimo.

---

## Visualización

Cada algoritmo genera dos gráficas:
- **Grafo del laberinto** (networkx): nodos coloreados según su rol.
- **Matriz coloreada** (matplotlib): vista directa sobre la cuadrícula.

| Color    | Significado              |
|----------|--------------------------|
| Blanco   | Espacio libre            |
| Negro    | Pared                    |
| Verde    | Celda de inicio          |
| Azul     | Celda meta               |
| Amarillo | Celda explorada          |
| Rojo     | Celda en el camino final |

---

## Requisitos e Instalación

### Requisitos
- Python 3.8 o superior
- Librerías: `matplotlib`, `networkx`, `numpy`

### Instalación de dependencias

```bash
pip install matplotlib networkx numpy
```

### Ejecución

```bash
python main.py
```

## Decisiones de Diseño

1. El laberinto se convierte a un **grafo dirigido con costos uniformes (peso 1)** usando lista de adyacencia, lo que permite aplicar los tres algoritmos de forma uniforme.
2. La **heurística se precalcula** para todos los nodos transitables antes de ejecutar A\*, evitando cálculos repetidos durante la búsqueda.
3. La función `reconstruct_path` en `utils.py` es **compartida** por los tres algoritmos, reduciendo duplicación de código.
4. Cada algoritmo retorna tanto el **camino** como el **orden de exploración**, facilitando la visualización comparativa del comportamiento de cada estrategia.
