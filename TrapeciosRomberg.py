import numpy as np

def trapecios(f, a, b, n):
    h = (b - a) / n
    muestras = n + 1

    # calcula el área del trapecio
    sum = 0
    xi = a
    for i in range(0, n, 1):
        metodoTrapecio = (h / 2) * (f(xi) + f(xi + h))
        sum += metodoTrapecio
        xi += h

    print("\nResultado de la integral por el método de trapecios: " + str(sum) + "\n")


def romberg(f, a, b, n):
    h = (b - a) / 2 ** n
    B = b + h  # para que en xi incluya el valor de b

    xi = np.arange(a, B, h)  # genera todos los x
    # print(xi)
    print("\nLos puntos son: " + str(xi))

    trapeciosT = []  # guarda todos los T obtenidos

    # TRAPECIOS
    subH = 1
    for i in range(n + 1):
        sumfx = 0
        for j in range(0, len(xi), subH):
            if (xi[j] != a and xi[j] != b):
                sumfx += 2 * (f(xi[j]))
            else:
                sumfx += f(xi[j])
            totalTrapecios = ((subH * h) / 2) * sumfx

        trapeciosT.append(totalTrapecios)
        print("\nT" + str(subH) + "h = " + str(totalTrapecios))
        subH *= 2  # incrementa el valor de Tnh siendo siempre múltiplo de 2 (h, 2h, ..., 8h)

    # PRIMER PASO ROMBERG
    print("\nROMBERG: Primer paso")
    Th = ((4 * trapeciosT[0]) - trapeciosT[1]) / 3
    print("\nTh = " + str(Th))
    T2h = ((4 * trapeciosT[0]) - trapeciosT[1]) / 3
    print("\nTh = " + str(Th))

    # SEGUNDO PASO ROMBERG
    print("\nROMBERG: Segundo paso")
    TH = ((16 * Th) - T2h) / 15
    print("\nEl resultado de la integral por el método de Romberg es " + str(TH))

# testeo de los métodos
trapecios(lambda x: np.power((x+5),2), -1, 1, 3)
romberg(lambda x: np.power(x,3), 2, 4, 3)