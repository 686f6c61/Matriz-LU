import numpy as np

# Descomposición LU para matrices cuadradas

# Solicita el tamaño de la matriz cuadrada (número de filas y columnas)
m = int(input("Introduce el número de filas = número de columnas: "))

# Inicializamos las matrices que serán usadas: matriz original (matriz), matriz superior (u) y matriz inferior (l)
matriz = np.zeros([m, m])  # Matriz original
u = np.zeros([m, m])       # Matriz superior U
l = np.zeros([m, m])       # Matriz inferior L

# Solicita los elementos de la matriz al usuario
print("Introduce los elementos de la matriz")

# Rellenamos la matriz original con los valores proporcionados por el usuario
for r in range(m):
    for c in range(m):
        matriz[r, c] = float(input(f"Elemento a[{r+1},{c+1}]: "))  # Se lee y convierte cada elemento a float
        u[r, c] = matriz[r, c]  # Inicialmente, la matriz U es igual a la original

# Procedemos a realizar la descomposición LU
for k in range(m):
    for r in range(m):
        if k == r:
            # La diagonal principal de la matriz L debe ser 1
            l[k, r] = 1
        if k < r:
            # Calculamos el factor para hacer ceros debajo de la diagonal
            factor = matriz[r, k] / matriz[k, k]
            l[r, k] = factor  # Guardamos el factor en L

            # Restamos el múltiplo de la fila superior para hacer el elemento (r,k) de U igual a cero
            for c in range(m):
                matriz[r, c] = matriz[r, c] - (factor * matriz[k, c])
                u[r, c] = matriz[r, c]  # Actualizamos la matriz U con los nuevos valores

# Resultados de la descomposición LU
print("Resultados:")
print("Matriz L (inferior):")
print(l)

print("Matriz U (superior):")
print(u)

# Comprobación: multiplicamos las matrices L y U para verificar que el resultado sea la matriz original
matriz_reconstruida = np.zeros([m, m])  # Inicializamos la matriz reconstruida

# Producto L*U para verificar
for r in range(m):
    for c in range(m):
        for k in range(m):
            matriz_reconstruida[r, c] += l[r, k] * u[k, c]  # Suma de productos L*U

# Mostramos la matriz reconstruida
print("Matriz reconstruida a partir de L y U:")
print(matriz_reconstruida)

# Alternativa más sencilla usando np.dot para multiplicar L y U
a = np.dot(l, u)
print("Matriz reconstruida usando np.dot:")
print(a)
