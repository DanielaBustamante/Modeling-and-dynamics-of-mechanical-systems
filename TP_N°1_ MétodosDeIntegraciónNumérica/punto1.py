import numpy as np
import matplotlib.pyplot as plt

# Metodo del trapecio
at = 1
bt = 2
n = 10 # número de subintervalos
dx = (bt - at) / n
I = np.zeros((n, 1))
It = 0
def fx(x):
    return ((4-x**2) ** (1/2)) / (5-x**2)
for i in range(n):
    a = at + i * dx
    b = a + dx
    I[i] = (fx(a) + fx(b)) * dx / 2
for j in range(n):
    It = It + I[j]
print("Por el metodo de trapecio da:", It)

# Metodo del punto medio
at = 1
bt = 2
n = 10 # número de subintervalos
dx = (bt - at) / n
I = np.zeros((n, 1))
It = 0
def fx(x):
    return ((4-x**2) ** (1/2)) / (5-x**2)
for i in range(n):
    a = at + i * dx
    b = a + dx
    m = (a + b) / 2
    I[i] = fx(m) * dx
for j in range(n):
    It = It + I[j]
print("Por el metodo del punto medio da:", It)

# Metodo de simpson
at = 1
bt = 2
n = 10 # número de subintervalos
dx = (bt - at) / n
I = np.zeros((n, 1))
It = 0
def fx(x):
    return ((4-x**2) ** (1/2)) / (5-x**2)
for i in range(n):
    a = at + i * dx
    b = a + dx
    m = (a + b) / 2
    I[i] = (fx(a) + 4*fx(m) + fx(b)) * dx / 6
for j in range(n):
    It = It + I[j]
print("Por el metodo de simpson da:", It)

# Grafico
# Crear un arreglo de valores de x
x = np.linspace(1, 2, 1000)
# Evaluar la función en los valores de x
y = fx(x)
# Graficar los puntos
plt.plot(x, y)
plt.title('Gráfico de la función')
plt.xlabel('x')
plt.ylabel('y')
plt.show()