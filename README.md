# Descomposición LU con NumPy

Este proyecto implementa la descomposición LU de una matriz cuadrada utilizando NumPy. La descomposición LU es un método para descomponer una matriz en el producto de una matriz triangular inferior (L) y una matriz triangular superior (U).

## Descripción

El script solicita al usuario que ingrese una matriz cuadrada y luego realiza la descomposición LU, generando las matrices L y U. Además, el código realiza una comprobación multiplicando las matrices L y U para verificar que se obtiene la matriz original.

## Requisitos

Para ejecutar este proyecto necesitas tener instalado:

- **NumPy**: Para el manejo de matrices.


## Explicación del Código
Entrada de la matriz: El usuario ingresa el tamaño de la matriz cuadrada y sus elementos.
Descomposición LU: El script utiliza un método de eliminación para generar las matrices L (triangular inferior) y U (triangular superior).
Comprobación: Multiplica las matrices L y U para verificar que el resultado coincide con la matriz original.
Método alternativo: También se incluye la función np.dot() para calcular la multiplicación de las matrices L y U.
Resultados
El script imprimirá:

La matriz L (triangular inferior).
La matriz U (triangular superior).
La matriz original reconstruida a partir de la multiplicación L * U.


## Ejemplo de Uso

Introduce el número de filas = número de columnas: 3
Introduce los elementos de la matriz:
Elemento a[1,1]: 2
Elemento a[1,2]: 3
Elemento a[1,3]: 1
Elemento a[2,1]: 4
Elemento a[2,2]: 7
Elemento a[2,3]: 3
Elemento a[3,1]: 6
Elemento a[3,2]: 10
Elemento a[3,3]: 4

## Licencia
Este proyecto está bajo la Licencia MIT. Puedes encontrar más detalles en el archivo LICENSE.








