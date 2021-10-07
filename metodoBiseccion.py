import math

def f(x):
    return (math.e)**(3*x)-4 #funcion de prueba

def biseccion(a, b, err):
    i = 0 #contador para las iteraciones
    err = err * 100 #error ingresado y lo pasamos a %
    e = ((b - a) / 2) * 100 #error calculado en base a los datos ingresados

    while e > err: #hasta que el error calculado no sea menor al solicitado se va a iterar
        m = (a + b) / 2
        if f(a) * f(m) > 0:
            a = m
        else:
            b = m
        e = ((b - a) / 2) * 100
        i += 1

    print("La raiz aproximada es x = " + str(m) + ", con un error de " + str(e) + "%")

biseccion(0,1,0.01)