import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import *
init_printing(use_latex=True)

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

     trapeciosT = []

     subH = 1
     for i in range(n):
         sumfx = 0
         #print(" --- ")
         subH *= 2
         for j in range(0, len(xi), subH):
             #print(xi[j])
             if(xi[j] != a and xi[j] != b):
                 sumfx += 2 * (fx(xi[j]))
             else:
                 sumfx += fx(xi[j])

             #print(sumfx)
             totalTrapecios = ((subH * h) / 2) * sumfx

         trapeciosT.append(totalTrapecios)
         #print("TOTAL " + str(totalTrapecios))



romberg(sp.Pow(x,3), 2, 4, 3)





