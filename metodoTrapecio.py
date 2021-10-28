import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import *
init_printing(use_latex=True)

x = sp.Symbol("x")

def trapecios(f, a, b, n):
     integral = sp.Integral(f, (x, a, b))
     print("\nLa integral a resolver es:\n")
     pprint(integral)

     rtaInteg = sp.integrate(f, (x, a, b))
     print("\nIntegrando el resultado es:\n")
     pprint(rtaInteg)

     expr = f
     fx = lambdify(x, expr, "numpy")

     h = (b - a) / n
     muestras = n + 1

     sum = 0
     xi = a
     for i in range(0, n, 1):
          metodoTrapecio = (h/2) * (fx(xi) + fx(xi+h))
          sum += metodoTrapecio
          xi += h

     xi = np.linspace(a, b, muestras)
     fi = fx(xi)

     muestrasLinea = muestras * 5
     xL = np.linspace(a, b, muestrasLinea)
     fL = fx(xL)

     plt.plot(xi, fi, "o", color="red")
     plt.plot(xL, fL, color="black")
     plt.fill_between(xi, 0, fi, color="blue")
     for i in range(0, muestras, 1):
          plt.axvline(xi[i], color="green")
     plt.show()

     print("\nResultado de la integral por el método de trapecios: " + str(sum) + "\n")

trapecios(sp.Pow(x,2), 0, 1, 3)

