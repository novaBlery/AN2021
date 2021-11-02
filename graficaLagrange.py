import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def grafico(xi, fi):
    x = sp.Symbol("x")  # variable simbolica
    interpLag = 0

    for i in range(0, len(xi)):
        numerador = 1
        denominador = 1
        for j in range(0, len(xi)):
            if i != j:
                numerador *= (x - xi[j])
                denominador *= (xi[i] - xi[j])

            polinomio = (numerador / denominador) * fi[i]

        interpLag += polinomio

    # gráfica de la integral obtenida por el método de trapecios
    px = sp.lambdify(x, interpLag)
    puntos_xi = np.linspace(np.min(xi), np.max(xi), 100)  # para que el grafico quede curvado
    puntos_fi = px(puntos_xi)
    plt.plot(xi, fi, "o", color="red")
    plt.plot(puntos_xi, puntos_fi, color="black")
    plt.title('Interpolación de Lagrange')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
