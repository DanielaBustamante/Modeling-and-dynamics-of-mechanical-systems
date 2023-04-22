import numpy as np

# Definimos los datos de la tabla como arrays de numpy
x = np.array([1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60, 1.70, 1.80, 1.90, 2.00])
f = np.array([2.7183, 3.0042, 3.3201, 3.6693, 4.0552, 4.4817, 4.9530, 5.4739, 6.0496, 6.6859, 7.3891])

# Definimos los límites de integración
a, b = 1, 2

# Calculamos la integral definida utilizando el método de trapecios
dx = (b - a) / (len(x) - 1)
integral_trapezoid = dx / 2 * (f[0] + 2 * np.sum(f[1:-1]) + f[-1])
print("Integral definida (trapecios):", integral_trapezoid)

# Calculamos la integral definida utilizando el método de punto medio
dx = (b - a) / len(x)
integral_midpoint = dx * np.sum(f[:-1] + f[1:]) / 2
print("Integral definida (punto medio):", integral_midpoint)

# Calculamos la integral definida utilizando el método de Simpson
n = len(x) - 1
dx = (b - a) / n
x_nodes = np.linspace(a, b, n+1)
f_nodes = np.interp(x_nodes, x, f)
integral_simpson = dx / 3 * (f_nodes[0] + 4 * np.sum(f_nodes[1:-1:2]) + 2 * np.sum(f_nodes[2:-1:2]) + f_nodes[-1])
print("Integral definida (Simpson):", integral_simpson)