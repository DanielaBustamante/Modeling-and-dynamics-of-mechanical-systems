import numpy as np

# PUNTO 2A
print("Sean las siguientes matrices:")
print('A = [0, 4, -7, 5], [4, 0, -1, 0], [6, 4, -6, 8], [-2, 2, 6, 9]')
print('B =[2, 4, -7, 5], [4, 0, -1, 0], [6, 4, -6, 8], [-2, -4, 7, -5]')
print('C= [2, 4, -7, 0], [4, 3, -1, 0], [6, 4, -6, 0], [-2, 2, 6, 0]')
A = np.array([[0, 4, -7, 5], [4, 0, -1, 0], [6, 4, -6, 8], [-2, 2, 6, 9]])
B = np.array([[2, 4, -7, 5], [4, 0, -1, 0], [6, 4, -6, 8], [-2, -4, 7, -5]])
C = np.array([[2, 4, -7, 0], [4, 3, -1, 0], [6, 4, -6, 0], [-2, 2, 6, 0]])
# ¿Qué condición se debe dar para que en una matriz exista el determinante?
# Para que una matriz cuadrada tenga determinante, se requiere que la matriz sea no singular, es decir, que su determinante sea diferente de cero.
print('')
print("El determinante de A es:", int(np.linalg.det(A)))
print("El determinante de B es:", int(np.linalg.det(B)))
print("El determinante de C es:", int(np.linalg.det(C)))
# Con el resultado obtenido, ¿Es posible obtener la matriz inversa?
# Si es distinto de 0 podemos calcular la matriz inversa.
print('')
try:
    print("La inversa de A es:\n", np.linalg.inv(A))
except np.linalg.LinAlgError:
    print("La inversa de A no se puede calcular debido a que su determinante es cero.")
try:
    print("La inversa de B es:\n", np.linalg.inv(B))
except np.linalg.LinAlgError:
    print("La inversa de B no se puede calcular debido a que su determinante es cero.")
try:
    print("La inversa de C es:\n", np.linalg.inv(C))
except np.linalg.LinAlgError:
    print("La inversa de C no se puede calcular debido a que su determinante es cero.")

# PUNTO 2B
# b) Si no es posible, ¿qué habría que modificar para que sea posible? Si es así modificarlo. Justificar.
# Para hacer que una matriz sea invertible, debemos modificarla para que tenga un determinante distinto de cero.
# Esto se puede lograr agregando o eliminando filas o columnas según sea necesario.

# PUNTO 2C
# c) Calcular la traspuesta y la inversa de cada matriz.
# Dejando la última fila toda positiva:
print('')
B_nueva = np.array([[2, 4, -7, 5], [4, 0, -1, 0], [6, 4, -6, 8], [-2, -4, -7, -5]])
print("La traspuesta de la nueva matriz B es:\n", np.transpose(B_nueva))
try:
    print("La inversa de la nueva matriz B es:\n", np.linalg.inv(B_nueva))
except np.linalg.LinAlgError:
    print("La inversa de la nueva matriz B no se puede calcular debido a que su determinante es cero.")
# Cambiando la columna de ceros por 1:
print('')
C_nueva = np.array([[2, 4, -7, 1], [4, 3, -1, 2], [6, 4, -6, 3], [-2, 2, 6, 4]])
print("La traspuesta de la nueva matriz C es:\n", np.transpose(C_nueva))
try:
    print("La inversa de la nueva matriz C es:\n", np.linalg.inv(C_nueva))
except np.linalg.LinAlgError:
    print("La inversa de la nueva matriz C no se puede calcular debido a que su determinante es cero.")
print('')

# PUNTO 2D
# d) Obtener los siguientes vectores fila de cada matriz:
# d1=[diagonal principal]  
print("La diagonal principal de A es")
print(np.diag(A))
print("La diagonal principal de B_nueva es")
print(np.diag(B_nueva))
print("La diagonal principal de C_nueva es")
print(np.diag(C_nueva))
print('')
# d2=[fila 3]  
print("La fila 3 de A es")
print(A[2,:])
print("La fila 3 de B_nueva es")
print(B_nueva[3,:])
print("La fila 3 de C_nueva es")
print(C_nueva[3,:])
print('')
# d3=[columna 3]  
print("La columna 3 de A es")
print(A[:,3])
print("La columna 3 de B_nueva es")
print(B_nueva[:,3])
print("La columna 3 de C_nueva es")
print(C_nueva[:,3])
print('')

# PUNTO 2E
# e) Obtener las siguientes matrices de cada matriz:
# e1=[filas 1 y 2 x columnas 2 y 3]
print("Las filas 1 y 2 de cada matriz:")
A_filas1y2 = np.concatenate((A[0:2, :],))
B_nueva_filas1y2 = np.concatenate((B_nueva[0:2, :],))
C_nueva_filas1y2 = np.concatenate((C_nueva[0:2, :],))

print("Las columnas 2 y 3 de cada matriz:")
A_columnas2y3 = A[:, 1:3]
B_nueva_columnas2y3 = B_nueva[:, 1:3]
C_nueva_columnas2y3 = C_nueva[:, 1:3]

print("Las matrices obtenidas de multiplicar las filas 1 y 2 por columnas 2 y 3:")
Matriz1 = np.dot(A_filas1y2, A_columnas2y3)
Matriz2 = np.dot(B_nueva_filas1y2, B_nueva_columnas2y3)
Matriz3 = np.dot(C_nueva_filas1y2, C_nueva_columnas2y3)

# e2=[filas 3 y 4 x columnas 2 y 3]
print("Las filas 3 y 4 de cada matriz:")
A_filas3y4 = np.concatenate((A[2:4, :],))
B_nueva_filas3y4 = np.concatenate((B_nueva[2:4, :],))
C_nueva_filas3y4 = np.concatenate((C_nueva[2:4, :],))

print("Las matrices obtenidas de multiplicar las filas 3 y 4 por columnas 2 y 3:")
Matriz4 = np.dot(A_filas3y4, A_columnas2y3)
Matriz5 = np.dot(B_nueva_filas3y4, B_nueva_columnas2y3)
Matriz6 = np.dot(C_nueva_filas3y4, C_nueva_columnas2y3)

# e3=[columnas 1 y 4 x filas 3 y 4]
print("Las columnas 1 y 4 de cada matriz:")
A_columnas1y4 = A[:, [0, 3]]
B_nueva_columnas1y4 = B_nueva[:, [0, 3]]
C_nueva_columnas1y4 = C_nueva[:, [0, 3]]

print("Las filas 3 y 4 de cada matriz:")
A_filas3y4 = np.concatenate((A[2:4, :],))
B_nueva_filas3y4 = np.concatenate((B_nueva[2:4, :],))
C_nueva_filas3y4 = np.concatenate((C_nueva[2:4, :],))

print("Las matrices obtenidas de multiplicar las columnas 1 y 4 por filas 3 y 4:")
Matriz7 = np.dot(A_filas3y4, A_columnas1y4)
Matriz8 = np.dot(B_nueva_filas3y4, B_nueva_columnas1y4)
Matriz9 = np.dot(C_nueva_filas3y4, C_nueva_columnas1y4)