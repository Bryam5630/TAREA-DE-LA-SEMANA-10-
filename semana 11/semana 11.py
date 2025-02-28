# Deber de la semana 11: Primero vamos a crear una matriz bidimensional

listlista = [
    [3, 2, 6],
    [4, 5, 7],
    [6, 8, 9]
]

numero_buscado = int(input("Escoge un número de la matriz: "))

# Buscar el número en la matriz usando un for
for i in range(3):  # Recorre las filas
    for j in range(3):  # Recorre las columnas
        if listlista[i][j] == numero_buscado:
            print(f"Está en la fila {i}, columna {j}.")
            break  # Sale del segundo for
    else:
        continue  # Si no se encuentra el número, sigue con la siguiente fila
    break  # Si se encuentra, sale del primer for

else:
    print("No está en la matriz.")