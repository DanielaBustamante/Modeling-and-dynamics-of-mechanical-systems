# PUNTO 1A
import csv
# Abrir el archivo CSV en modo de lectura y escritura
with open('trabajo_optativo_1/tabla_temperaturas.csv', 'r+', newline='') as tabla_temperaturas:
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
    with open('trabajo_optativo_1/Promedios.csv', 'w', newline='') as tabla_actualizada:
        # Escribir los encabezados de las columnas en el archivo actualizado
        csv_writer = csv.writer(tabla_actualizada)
        csv_writer.writerow(encabezados)
        # Escribir las filas actualizadas en el archivo actualizado
        csv_writer.writerows(filas_actualizadas)

# PUNTO 1B
import pandas as pd
# Leer archivo CSV
data = pd.read_csv('trabajo_optativo_1/tabla_temperaturas.csv')
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
data = pd.read_csv('trabajo_optativo_1/promedios.csv')
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
import pandas as pd
import matplotlib.pyplot as plt
# Carga el archivo CSV en un DataFrame de pandas
df = pd.read_csv('trabajo_optativo_1/promedios.csv')
# Crea el gráfico con etiquetas en los ejes y una grilla reticulada
ax = df.plot(x='Dia', y=['Min', 'Max', 'promedio'])
ax.set_xlabel('Dias')
ax.set_ylabel('Temperaturas')
ax.set_title('Febrero de 2019 en Bs. As.')
ax.grid(True)
# Muestra el gráfico en la pantalla o guarda el gráfico en un archivo
plt.show()