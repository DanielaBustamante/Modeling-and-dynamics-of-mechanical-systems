#Sea la siguiente grilla con los valores de temperatura en grados centígrados de una placa en el instante t=0, 
# siendo los valores x e y distancias dadas en metros x 10-2.

# a) Obtener el grafico de curva de nivel correspondiente a dicha grilla. 
# Dar colores a cada nivel y mostrar la barra de colores de referencia, colocar título y etiquetas en los ejes. 

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Leer los datos del archivo CSV
data = np.genfromtxt('Trabajo N°1/grilla_temperaturas.csv', delimiter=',')

# Extrae las columnas x e y de los datos leídos
x = data[:, 0]
y = data[:, 1]

# Extrae la columna de los valores z de los datos leídos
z = data[:, 2]

# Identifica y elimina los valores faltantes en los datos utilizando la función isnan de numpy
mask = ~(np.isnan(x) | np.isnan(y) | np.isnan(z))
x = x[mask]
y = y[mask]
z = z[mask]

# Crea una cuadrícula de coordenadas xi y yi utilizando la función meshgrid de numpy
xi = np.linspace(0, 10, 101)
yi = np.linspace(0, 10, 101)
xi, yi = np.meshgrid(xi, yi)

# Interpola los valores de z para las coordenadas xi e yi utilizando la función griddata de scipy
zi = griddata((x, y), z, (xi, yi), method='linear')

# Crea el gráfico de curvas de nivel utilizando la función contour de matplotlib
contour = plt.contour(xi, yi, zi, levels=10)

# Establece los valores y etiquetas para los ticks en los ejes x e y utilizando las funciones xticks y yticks
plt.xticks(np.arange(0, 11, 2))
plt.yticks(np.arange(0, 11, 2))

# Agrega una etiqueta para el eje x y y utilizando las funciones xlabel y ylabel
plt.xlabel('x')
plt.ylabel('y')

# Agrega los valores de z como etiquetas de texto para cada curva de nivel
plt.clabel(contour, inline=True, fontsize=8)

# Muestra el gráfico
plt.show()

# b) Obtener los siguientes gráficos de temperatura en grados centígrados en función de la distancia en metros, 
# colocar título y etiquetas en los ejes.   b1: Diagonal x=y  b2: Línea y=5  b3: Línea x=5