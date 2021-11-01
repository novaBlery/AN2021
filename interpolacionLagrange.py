import sympy as sym

# definimos los valores de x y f(x)
xi = [1, 2, 3]
fi = [10, 15, 30]

x = sym.Symbol("x") # variable simbolica
i = 0

terminos_l = [] # recopila todos los L's calculados

for i in range(0, len(xi)):
    # se alamacenan los numeradores y denominadores de la iteracion para cada termino L
    numeradores_l = []
    denominadores_l = []

    for j in range(0, len(xi)):
        if i != j:
            numerador = ("(" + str(x - xi[j]) + ")")
            numeradores_l.append(numerador)
            denominador = (xi[i] - xi[j])
            denominadores_l.append(denominador)

    numeradores_str = " * ".join(map(str, numeradores_l))
    denominadores_str = " * ".join(map(str, denominadores_l))
    # la interpolacion de Lagrange pide una forma particular de L que es L = x-xj/xi-xj * f(x)
    termino_p = "[ " + " ( " + numeradores_str + " ) " + " / " + " ( " + denominadores_str + " ) " + "]" + " * " +str(fi[i])
    terminos_l.append(termino_p)

polinomio = " + ".join(map(str, terminos_l)) # se unen los L obtenidos para formar el polinomio interpolante
print("El polinomio interpolante es: \n" + polinomio)




