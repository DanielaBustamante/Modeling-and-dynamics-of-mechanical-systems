#Sea la siguiente grilla con los valores de temperatura en grados centígrados de una placa en el instante t=0, 
# siendo los valores x e y distancias dadas en metros x 10-2.

# a) Obtener el grafico de curva de nivel correspondiente a dicha grilla. 
# Dar colores a cada nivel y mostrar la barra de colores de referencia, colocar título y etiquetas en los ejes. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Leer los datos del archivo CSV
df = pd.read_csv('Trabajo N°1/grilla_temperaturas.csv')

# Convertir los datos en una matriz numpy
data = df.values

# Obtener los valores de x, y y z
x = data[:,0]
y = data[:,1]
z = data[:,2]

# Definir los valores de x y y para la cuadrícula
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)

# Crear una cuadrícula de coordenadas xi y yi
X, Y = np.meshgrid(xi, yi)

# Obtener los valores de z para cada par de coordenadas xi, yi
Z = griddata((x, y), z, (X, Y), method='linear')

# Crear un gráfico de curvas de nivel
plt.contour(X, Y, Z)
plt.show()

# b) Obtener los siguientes gráficos de temperatura en grados centígrados en función de la distancia en metros, 
# colocar título y etiquetas en los ejes.   b1: Diagonal x=y  b2: Línea y=5  b3: Línea x=5
