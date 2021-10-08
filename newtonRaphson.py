import numpy as np

fx = lambda x: (1/np.exp(x))-x
dfx = lambda x: -(np.exp(-x))-1

def newtonRaphson(x0, err):
    err = err*100
    x = x0-fx(x0)/dfx(x0)
    e = abs((x-x0)/x)*100

    while e > err:
        x0 = x
        x = x0-fx(x0)/dfx(x0)
        e = abs((x-x0)/x)*100

    print("La raiz aproximada es " + str(x) + ", con un error de " + str(e) + "%")

newtonRaphson(0,0.01)