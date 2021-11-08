import numpy as np

matriz_a = np.array([[-2, 0, -2], [2, 2, 4], [0, 1, 0]])
matriz_b = np.array([[-10], [16], [0]])
matriz_ab = np.concatenate((matriz_a, matriz_b), axis=1) # Matriz aumentada
print("Matriz aumentada " + "\n" + str(matriz_ab) + "\n")


def proceso_descendente(matriz):

    for iteracion_p in range(len(matriz)):

        matriz_resultante = matriz.copy()

        # lo primero es definir el pivote, que tiene la forma matriz_a[p, p]
        pivote = matriz[iteracion_p, iteracion_p]

        for i in range(iteracion_p, len(matriz)):
            for j in range(iteracion_p, len(matriz) + 1):

                if i == iteracion_p:
                    # una vez en la posicion del pivote, lo segundo es dividir a la fila entera por el pivote
                    for k in range(len(matriz) + 1):
                        if pivote == 0:
                            continue
                        matriz_resultante[i, k] = matriz[i, k] / pivote
                    break

                else:
                    matriz_resultante[i, j] = matriz[i, j] - (
                                matriz[i, iteracion_p] * (matriz[iteracion_p, j] / pivote))

        matriz = matriz_resultante

    print("Proceso descendente\n", matriz)
    return matriz













