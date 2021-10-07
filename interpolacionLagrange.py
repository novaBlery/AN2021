import sympy as sym
import numpy as np

# definimos los valores de x y f(x)
xi = np.array([1, 2, 3])
fi = np.array([10, 15, 30])

x = sym.Symbol("x") # variable simbolica
i = 0

terminos_l = [] # recopila todos los L's calculados

for i in range(0, len(xi)):
    numeradores_l = [] # se alamacenan los numeradores de la iteracion
    denominadores_l = [] # se alamacenan los denominadores de la iteracion

    for j in range(0, len(xi)):
        if i != j:
            numerador = (x - xi[j])
            numeradores_l.append(numerador)
            denominador = (xi[i] - xi[j])
            denominadores_l.append(denominador)

    numerador_str = " * ".join(map(str, numeradores_l)) # se unen los numeradores obtenidos para cada L
    denominador_str = " * ".join(map(str, denominadores_l)) # se unen los denominadores obtenidos para cada L
    p = "( " + numerador_str + " / " + denominador_str + ")" + " * " +str(fi[i]) # forma de L -> num/den * f(x)
    terminos_l.append(p)

polinomio = " + ".join(map(str, terminos_l)) # se unen los L obtenidos para formar el polinomio interpolante
print("El polinomio interpolante es: \n" + polinomio)


