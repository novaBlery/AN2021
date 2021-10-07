import numpy as np

gx = lambda x: 0.4*np.exp(x**2) # se ingresa x = g(x) -> el despeje de la funcion

def puntoFijo(xi, err):
    err = err * 100
    x = gx(xi) # se calcula xi+1 = g(xi)
    e = abs((x - xi)/x)*100

    while e > err:
        xi = x
        x = gx(xi)
        e = abs((x - xi)/x)*100

    print("La raiz aproximada es " + str(x) + ", con un error de " + str(e) + "%")

puntoFijo(0,0.01)


