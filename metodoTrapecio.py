import sympy as sp
from sympy import init_printing #se utiliza para renderizar los resultados
init_printing(use_latex=True)
from sympy import pprint

n = 3
a = 0
b = 1
h = (b-a)/n

x = sp.Symbol("x")

integral = sp.Integral(sp.Pow(x,2),(x,a,b))
print("\nLa integral a resolver es:\n")
pprint(integral)

f = sp.integrate(sp.Pow(x,2),(x,a,b))
print("\nIntegrando el resultado es:\n")
pprint(f)

subIntervalos = []

intervalo = a
for i in range(n-1):
    intervalo = intervalo + h
    subIntervalos.append(intervalo)

sum = 0
for i in subIntervalos:
    x = i
    rta = 2 * sp.Pow(x, 2)
    sum += rta

trapecios = (h/2) * (sp.Pow(a, 2) + sum + sp.Pow(b,2))

print("\nAplicando el método de trapecios el resultado es: " + str(trapecios) + "\n")

error = abs(trapecios-f)

print("\nEl error absoluto es: " + str(error) + "\n")
