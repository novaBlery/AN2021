import math

def f(x):
    return (math.e)**(3*x)-4 # funcion de prueba

def biseccion(a, b, err):
    i = 0
    err = err * 100 # es el margen de error que se quiere mantener para la aproximacion
    e = ((b - a) / 2) * 100 # permite controlar el error actual que se tiene para compararlo con err

    # como se quiere llegar a un error menor al deseado se iterara hasta que esta condicion no se cumpla
    while e > err:
        m = (a + b) / 2
        if f(a) * f(m) > 0:
            a = m
        else:
            b = m
        e = ((b - a) / 2) * 100
        i += 1

    print("La raiz aproximada es x = " + str(m) + ", con un error de " + str(e) + "%")

biseccion(0,1,0.01)