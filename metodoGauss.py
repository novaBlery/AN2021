import numpy as np

matriz_a = np.array([[-2, 0, -2], [2, 2, 4], [0, 1, 0]])
matriz_b = np.array([[-10], [16], [0]])
matriz_ab = np.concatenate((matriz_a, matriz_b), axis=1) # Matriz aumentada
print("Matriz aumentada " + "\n" + str(matriz_ab) + "\n")


for iteracion_p in range(len(matriz_ab)):

    matriz_resultante = matriz_ab.copy()

    # lo primero es definir el pivote, que tiene la forma matriz_a[p, p]
    pivote = matriz_ab[iteracion_p, iteracion_p]

    for i in range(iteracion_p, len(matriz_ab)):
        for j in range(iteracion_p, len(matriz_ab) + 1):

            if i == iteracion_p:
                # una vez en la posicion del pivote, lo segundo es dividir a la fila entera por el pivote
                for k in range(len(matriz_ab) + 1):
                    if pivote == 0:
                        continue
                    matriz_resultante[i, k] = matriz_ab[i, k] / pivote
                break

            else:
                matriz_resultante[i, j] = matriz_ab[i, j] - (matriz_ab[i, iteracion_p] * (matriz_ab[iteracion_p, j] / pivote))

    matriz_ab = matriz_resultante

print(matriz_ab)













