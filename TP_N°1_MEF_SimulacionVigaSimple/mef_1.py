# Importamos las librerías que vamos a usar
import numpy
import matplotlib.pyplot as plt
# Modulo de Young en [Pa]
E = 2e+11
# Momento de Inercia respecto de IYY en [m^4]
Ir = 7.848e-7 # cambia segun el perfil
# Fuerza en [N]
F = -1000
# Longitud  en [m]
l = 1.5
# Momento flector [Nm]
M = F * l
# Distancia al eje neutro [m]
y = 0.04 # mitad del Y
# Máximo desplazamiento en [mm], por eso se multiplica x 1000
Md = (F * l ** 3) / (3 * E * Ir) * 1000
# Máxima tensión en [MPa], por eso multiplica x1e-6
Me = ((M * y) / Ir) * 1e-6
# Creamos un vector equidistante en 100 tramos (definición por defecto) de [0,l]
x = numpy.linspace(0, l, 100)
# Calculamos el desplazamiento para todos los puntos definidos anteriormente
dis = (F * x ** 2) * (3 * l - x) * (1 / (6 * E * Ir)) * 1000
# Imprimimos los valores de desplazamiento y tensión
print("El máximo desplazamiento es:",Md,"en [mm]")
print("La tensión máxima es:",Me,"en [MPa]")
# Graficamos los puntos con sus respectivos desplazamientos
plt.plot(x, dis)
# Agregamos nombres a los ejes y un título al gráfico
plt.xlabel('Longitud (m)')
plt.ylabel('Desplazamiento (mm)')
plt.title('Desplazamiento de la viga')
# Muestro el gráfico
plt.show()