import numpy as np

def fx(x):
    return 2*x**3+3*x-5

def integral_trapecio(n=1, funcion=fx, err=0.1, at=1, bt=1, integral_calculada=1):
    error_actual = 1.0
    while error_actual > err:
        dx = (bt - at) / n
        I = np.zeros(n)
        It = 0
        for i in range(n):
            a = at + i * dx
            b = a + dx
            I[i] = (fx(a) + fx(b)) * dx / 2
        for j in range(n):
            It = It + I[j]
        error_actual = np.abs(integral_calculada - It)
        n += 1
    return n

def integral_simpson(n=1, funcion=fx, err=0.1, at=1, bt=1, integral_calculada=1):
    error_actual = 1.0
    while error_actual > err:
        dx = (bt - at) / n
        I = np.zeros(n)
        It = 0
        for i in range(n):
            a = at + i * dx
            b = a + dx
            m = (a + b) / 2
            I[i] = (fx(a) + 4*fx(m) + fx(b)) * dx / 6
        for j in range(n):
            It = It + I[j]
        error_actual = np.abs(integral_calculada - It)
        n += 1
    return n

if __name__ == "__main__":
     n = integral_trapecio(
         n=1,
         funcion=fx,
         err=0.001,
         at=1,
         bt=3,
         integral_calculada=42
     )
     print("--------------------------------------------------")
     print(f"los intervalos por el metodo de Trapecial es: {n}")

     n2 = integral_simpson(
         n=1,
         funcion=fx,
         err=0.001,
         at=1,
         bt=3,
         integral_calculada=42
     )
     print("-------------------------------------------------")
     print(f"los intervalos por el metodo de Simpson es: {n2}")
     print("-------------------------------------------------")