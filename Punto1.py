import pandas as pd

# Leemos el archivo CSV y lo almacenamos en un dataframe
df = pd.read_csv('Tabla_temperaturas.csv')
   
# a) Generar una tercera columna con los promedios diarios.

# Calculamos el promedio de las columnas 2 y 3 para cada fila
promedios = df.iloc[:, 1:3].mean(axis=1)

# Agregamos la columna de promedios al dataframe
df['promedio'] = promedios

# Guardamos el dataframe con la columna adicional en un nuevo archivo CSV
df.to_csv('ruta/nuevo_archivo.csv', index=False)

# b) Encontrar los promedios de las temperaturas máximas y mínimas del mes. 

# c) Encontrar los máximos y mínimos locales de las tres columnas.

# d) Graficar los máximos, mínimos y promedios del mes en un solo gráfico. 
# Colocar título, etiquetas en los ejes y grilla reticulada. 
