# Definir la matriz 3x3
matriz = [
    [3, 2, 6],
    [7, 5, 4],  # Esta fila no está ordenada
    [6, 8, 9]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario qué fila ordenar (0, 1, o 2)
fila_a_ordenar = int(input("\n¿Qué fila deseas ordenar? (0, 1 o 2): "))

# Ordenar la fila seleccionada con Bubble Sort
for i in range(len(matriz[fila_a_ordenar])):
    for j in range(len(matriz[fila_a_ordenar]) - 1):
        if matriz[fila_a_ordenar][j] > matriz[fila_a_ordenar][j + 1]:
            matriz[fila_a_ordenar][j], matriz[fila_a_ordenar][j + 1] = matriz[fila_a_ordenar][j + 1], matriz[fila_a_ordenar][j]

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
