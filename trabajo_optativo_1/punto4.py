#Punto 4A
import numpy as np
print('Resolver los siguientes sistemas de forma matricial:')
# Si no es posible resolver alguno de ellos, mencionar por qué. Justificar.
# Efectuar un cambio en algún coeficiente para salvar esto y calcular.
# Justificar el cambio.
print('4.*X.^2-7.*X.^3+5.*X.^4=2')
print('4.*X.^1-1.*X.^3=-5') 
print('6.*X.^1+4.*X.^2-6.*X.^3+8.*X.^4=1') 
print('-2.*X.^1+2.*X.^2+6.*X.^3+9.*X.^4=9')
# Armamos la matriz de los coeficientes
A = np.array([[0, 4, -7, 5], [4, 0, -1, 0], [6, 4, -6, 8], [-2, 2, 6, 9]])
print('')
# Armamos el vector
A_vector = np.array([2, -5, 1, 9]).reshape(-1, 1)
print('Calculamos el determinante de la matriz de los coeficientes:')
Det = int(np.linalg.det(A))
print(Det)
print('')
print('Calculamos la inversa:')
Ai = np.linalg.inv(A)
print(Ai)
print('')
print('Solucion del sistema') # Calculo la solucion del sistema como Ai*B
Sol = Ai.dot(A_vector)
print(Sol.T)
print('')

#Punto 4B
print('Resolver los siguientes sistemas de forma matricial:')
print('2.*X.^1+4.*X.^2-7.*X.^3+5.*X.^4=8') 
print('4.*X.^1-1.*X.^3=3') 
print('6.*X.^1+4.*X.^2-6.*X.^3+8.*X.^4=-4') 
print('-2.*X.^1-4.*X.^2+7.*X.^3-5.*X.^4=-7')
print('')
B = np.array([[2, 4, -7, 5], 
              [4, 0, -1, 0], 
              [6, 4, -6, 8], 
              [-2, -4, 7, -5]])
# Armamos el vector
B_vector = np.array([8, 3, -4, -7]).reshape(-1, 1)
print('Calculamos el determinante de la matriz de los coeficientes')
# Calculamos el determinante
Det = int(np.linalg.det(B))
print(Det)
print('')
print('Como el deteminante es 0 NO podemos calcular la matriz inversa')
print('')
# Ponemos la ultima fila toda positiva
B_nueva = np.array([[2, 4, -7, 5], 
                    [4, 0, -1, 0], 
                    [6, 4, -6, 8], 
                    [2, 4, 7, 5]])
print('Calculamos el determinante de la matriz de los coeficientes nueva')
# Calculamos el determinante
Det = int(np.linalg.det(B_nueva))
print(Det)
print('')
print('Calculamos la inversa nueva')
Bi = np.linalg.inv(B_nueva)
print(Bi)
print('')
print('Solucion del sistema')
# Calculo la solucion del sistema como Ai*B
Sol = Bi.dot(B_vector)
print(Sol.T)