# PUNTO 3A
# a) Obtener el grafico de curva de nivel correspondiente a dicha grilla.
# Dar colores a cada nivel y mostrar la barra de colores de referencia, colocar título y etiquetas en los ejes.
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
plt.title('Grafico de temperaturas')
# Agrega los valores de z como etiquetas de texto para cada curva de nivel
plt.contourf(contour)
# plt.clabel(contour, inline=True, fontsize=8)
plt.colorbar()
# Muestra el gráfico
plt.show()

# PUNTO 3B
# b) Obtener los siguientes gráficos de temperatura en grados centígrados en función de la distancia en metros,
# b1: Diagonal x=y
# Extraer los valores de la diagonal
diag = np.diag(data)
# Crear una gráfica simple de los valores de la diagonal
plt.plot(diag, 'o')
plt.xlabel('Índice')
plt.ylabel('Temperatura')
plt.title('Valores de la diagonal x=y')
plt.show()
# b2: Línea y=5
# Extraer los valores correspondientes a la fila y=5
fila = data[5, :]
# Crear una gráfica simple de los valores de la fila
plt.plot(fila, 'o')
plt.xlabel('Índice')
plt.ylabel('Temperatura')
plt.title('Valores de la fila y=5')
plt.show()
# b3: Línea x=5
# Extraer los valores correspondientes a la columna x=5
columna = data[:, 5]
# Crear una gráfica simple de los valores de la columna
plt.plot(columna, 'o')
plt.xlabel('Índice')
plt.ylabel('Temperatura')
plt.title('Valores de la columna x=5')
plt.show()