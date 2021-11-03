import sympy as sp

x = sp.Symbol("x")

def newtonRaphson(f, x0, err):
    # datos de la funcion a aplicar el metodo y su derivada
    global x
    df = sp.diff(f)

    # convertimos la entrada en sympy a numpy para poder trabajar con ella
    fx = sp.lambdify(x, f, "numpy")
    dfx = sp.lambdify(x, df, "numpy")

    err = err*100
    x = x0-fx(x0)/dfx(x0)
    e = abs((x-x0)/x)*100

    while e > err:
        x0 = x
        x = x0-fx(x0)/dfx(x0)
        e = abs((x-x0)/x)*100

    print("La raiz aproximada es " + str(x) + ", con un error de " + str(e) + "%")

newtonRaphson((1 / sp.exp(x)) - x,0,0.01)

