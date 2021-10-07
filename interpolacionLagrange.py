import sympy as sym
import numpy as np

#definimos los valores de x y f(x)
xi = np.array([1,2,3])
fi = np.array([10,15,30])

n = len(xi)
x = sym.Symbol("x") #variable simbolica
i = 0

P = []

for i in range(0,n):
    Lnum = [] #se alamacenan los numeradores de la iteracion
    Lden = [] #se alamacenan los denominadores de la iteracion

    for j in range(0,n):
        if i != j:
            num = (x - xi[j])
            Lnum.append(num)
            den = (xi[i] - xi[j])
            Lden.append(den)

    numerador = " * ".join(map(str, Lnum)) #se unen los numeradores obtenidos para cada L
    denominador = " * ".join(map(str, Lden)) #se unen los denominadores obtenidos para cada L
    p = "( " + numerador + " / " + denominador + ")" + " * " +str(fi[i]) #forma de L -> num/den * f(x)
    P.append(p)

polinomio = " + ".join(map(str, P)) #se unen los L obtenidos para formar el polinomio interpolante
print("El polinomio interpolante es: \n" + polinomio)


