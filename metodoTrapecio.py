import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import *
init_printing(use_latex=True)

x = sp.Symbol("x")

def trapecios(f, a, b, n):
     # imprime la integral a resolver
     integral = sp.Integral(f, (x, a, b))
     print("\nLa integral a resolver es:\n")
     pprint(integral)

     # devuleve el resultado de la integral por el método de integración
     rtaInteg = sp.integrate(f, (x, a, b))
     print("\nIntegrando el resultado es:\n")
     pprint(rtaInteg)

     # covertimos la entrada en sympy a numpy para poder trabajar con ella
     expr = f
     fx = lambdify(x, expr, "numpy")

     h = (b - a) / n
     muestras = n + 1

     # calcula el área del trapecio
     sum = 0
     xi = a
     for i in range(0, n, 1):
          metodoTrapecio = (h/2) * (fx(xi) + fx(xi+h))
          sum += metodoTrapecio
          xi += h

     xi = np.linspace(a, b, muestras)
     fi = fx(xi)

     # grafica de la integral obtenida por el método de trapecios
     plt.plot(xi, fi, "o", color="red")
     plt.plot(xi, fi, color="black")
     plt.fill_between(xi, 0, fi, color="blue")
     for i in range(0, muestras, 1):
          plt.axvline(xi[i], color="green")
     plt.show()

     print("\nResultado de la integral por el método de trapecios: " + str(sum) + "\n")

     error = abs(sum - rtaInteg)

     print("\nEl error absoluto es: " + str(error) + "\n")

trapecios(sp.Pow((x+5),2), -1, 1, 3)

