import pandas as pd

# Leemos el archivo CSV y lo almacenamos en un dataframe
df = pd.read_csv('tabla_temperaturas.csv')
   
# a) Generar una tercera columna con los promedios diarios.

# Calculamos el promedio de las columnas 1 y 2 para cada fila
promedios = df.iloc[:, 0:2].mean(axis=1)

# Agregamos la columna de promedios al dataframe
df['promedio'] = promedios

# Guardamos el dataframe con la columna adicional en un nuevo archivo CSV
df.to_csv('promedio_temperaturas.csv', index=False)

# b) Encontrar los promedios de las temperaturas máximas y mínimas del mes. 

# c) Encontrar los máximos y mínimos locales de las tres columnas.

# d) Graficar los máximos, mínimos y promedios del mes en un solo gráfico. 
# Colocar título, etiquetas en los ejes y grilla reticulada. 
