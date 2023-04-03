# PUNTO 1A
import csv
# Abrir el archivo CSV en modo de lectura y escritura
with open('trabajo_N1/tabla_temperaturas.csv', 'r+', newline='') as tabla_temperaturas:
    # Leer el archivo CSV con el módulo csv
    csv_reader = csv.reader(tabla_temperaturas)
    # Obtener los encabezados de las columnas
    encabezados = next(csv_reader)
    # Agregar "promedio" como el encabezado de la tercera columna
    encabezados.append("promedio")
    # Crear una lista vacía para almacenar las filas actualizadas
    filas_actualizadas = []
    # Iterar sobre cada fila del archivo CSV
    for fila in csv_reader:
        # Convertir los valores de las primeras dos columnas a números y calcular el promedio
        Promedio = (float(fila[1]) + float(fila[2])) / 2
        # Agregar el promedio como un tercer valor en la fila
        fila.append(Promedio)
        # Agregar la fila actualizada a la lista de filas actualizadas
        filas_actualizadas.append(fila)
    # Escribir las filas actualizadas en un nuevo archivo CSV
    with open('trabajo_N1/promedios.csv', 'w', newline='') as tabla_actualizada:
        # Escribir los encabezados de las columnas en el archivo actualizado
        csv_writer = csv.writer(tabla_actualizada)
        csv_writer.writerow(encabezados)
        # Escribir las filas actualizadas en el archivo actualizado
        csv_writer.writerows(filas_actualizadas)

# PUNTO 1B
import pandas as pd
# Leer archivo CSV
data = pd.read_csv('trabajo_N1/tabla_temperaturas.csv')
column1 = data.iloc[1:28, 1]
# Calcular el promedio de la columna seleccionada.
promedio = column1.mean()
print("El promedio de las temperaturas maximas es:", promedio)
column2 = data.iloc[1:28, 2]
# Calcular el promedio de la columna seleccionada.
promedio = column2.mean()
print("El promedio de las temperaturas minimas es:", promedio)

# PUNTO 1C
# Leer archivo CSV
data = pd.read_csv('trabajo_N1/promedios.csv')
# Seleccionar las filas desde la fila 1 hasta la fila 28 y las columnas 1, 2 y 3.
selected_data = data.iloc[1:28, 1:3]
# Encontrar el valor máximo y mínimo de todas las columnas.
max_value = selected_data.max().max()
min_value = selected_data.min().min()
# Imprimir los valores máximos y mínimos.
print("Valor máximo: ", max_value)
print("Valor mínimo: ", min_value)

# PUNTO 1D
# Graficar los máximos, mínimos y promedios del mes en un solo gráfico. 
# Colocar título, etiquetas en los ejes y grilla reticulada.
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
# Leer los datos del archivo CSV
data = np.genfromtxt('./grilla_temperaturas.csv', delimiter=',')
# Extrae las columnas z, x, z de los datos leídos
x = data[1:11, 0]
y = data[0,1:11]
z = data[1:11, 1:11]
# Crea una cuadrícula de coordenadas xi y yi utilizando la función meshgrid de numpy
xi = np.linspace(0, 10, 10)
yi = np.linspace(0, 10, 10)
xi, yi = np.meshgrid(xi, yi)
# Crea el gráfico de curvas de nivel utilizando la función contour de matplotlib
contour = plt.contour(xi, yi, z, levels=10)
# Establece los valores y etiquetas para los ticks en los ejes x e y utilizando las funciones xticks y yticks
plt.xticks(np.arange(0, 11, 2))
plt.yticks(np.arange(0, 11, 2))
# Agrega una etiqueta para el eje x y y utilizando las funciones xlabel y ylabel
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafico de temperaturas maximas, minimas y promedios')
# Agrega los valores de z como etiquetas de texto para cada curva de nivel
plt.contourf(contour)
# plt.clabel(contour, inline=True, fontsize=8)
plt.colorbar()
# Muestra el gráfico
plt.show()
# Extraer los valores correspondientes a las columnas 1,2 y 3
columna = data[:, 1]
# Crear una gráfica simple de los valores de la fila
# Crear una gráfica simple de los valores de la columna
plt.plot(columna, 'o')
plt.xlabel('Índice')
plt.ylabel('Temperatura')
plt.title('Valores de la columna x=5')
plt.show()