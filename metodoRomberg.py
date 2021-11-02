import numpy as np
import sympy as sp
from sympy import *
init_printing(use_latex=True)
import matplotlib.pyplot as plt

x = sp.Symbol("x")

def romberg(f, a, b, n):

     # imprime la integral a resolver
     integral = sp.Integral(f, (x, a, b))
     print("\nLa integral a resolver es:\n")
     pprint(integral)

     # devuelve el resultado de la integral por el método de integración
     rtaInteg = sp.integrate(f, (x, a, b))
     print("\nIntegrando el resultado es:\n")
     pprint(rtaInteg)

     # convertimos la entrada en sympy a numpy para poder trabajar con ella
     expr = f
     fx = lambdify(x, expr, "numpy")

     h = (b - a) / 2**n
     B = b + h # para que en xi incluya el valor de b

     xi = np.arange(a, B, h) # genera todos los x
     #print(xi)
     print("\nLos puntos son: " + str(xi))

     trapeciosT = [] # guarda todos los T obtenidos

    # TRAPECIOS
     subH = 1
     for i in range(n+1):
         sumfx = 0
         for j in range(0, len(xi), subH):
             if(xi[j] != a and xi[j] != b):
                 sumfx += 2 * (fx(xi[j]))
             else:
                 sumfx += fx(xi[j])
             totalTrapecios = ((subH * h) / 2) * sumfx

         trapeciosT.append(totalTrapecios)
         print("\nT" + str(subH) + "h = " + str(totalTrapecios))
         subH *= 2 # incrementa el valor de Tnh siendo siempre múltiplo de 2 (h, 2h, ..., 8h)

     # PRIMER PASO ROMBERG
     print("\nROMBERG: Primer paso")
     Th = ((4 * trapeciosT[0]) - trapeciosT[1]) / 3
     print("\nTh = " + str(Th))
     T2h = ((4 * trapeciosT[0]) - trapeciosT[1]) / 3
     print("\nTh = " + str(Th))

     # SEGUNDO PASO ROMBERG
     print("\nROMBERG: Segundo paso")
     TH = ((16 * Th) - T2h) / 15
     print("\nEl resultado de la integral por el método de Romberg es " + str(TH))

     fi = fx(xi)
     # gráfica de la integral obtenida por el método de trapecios
     plt.plot(xi, fi, color="black")
     plt.fill_between(xi, 0, fi, color="blue")
     plt.title('Método de Romberg')
     plt.xlabel('x')
     plt.ylabel('y')
     plt.grid()
     plt.show()

romberg(sp.Pow(x,3), 2, 4, 3) #testeo







