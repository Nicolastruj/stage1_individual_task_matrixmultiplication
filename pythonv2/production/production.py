import random
import numpy as np
from scipy.sparse import random as sparse_random
from scipy.sparse import csc_matrix


def my_function(n):
    A = [[random.random() for _ in range(n)] for _ in range(n)]
    B = [[random.random() for _ in range(n)] for _ in range(n)]
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

def my_function2(n):
    A = np.random.random((n, n))
    B = np.random.random((n, n))
    C = np.dot(A, B)
    return C

def my_function3(n):
    A = np.random.random((n, n))
    B = np.random.random((n, n))
    C = A @ B
    return C

def my_function4(n):
    A = [[random.random() for _ in range(n)] for _ in range(n)]
    B = [[random.random() for _ in range(n)] for _ in range(n)]
    B_T = [[B[j][i] for j in range(n)] for i in range(n)]
    C = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B_T[j][k] for k in range(n))

    return C



def my_function5(n):
    A = sparse_random(n, n, density=0.5, format='csc').A  # Genera una matriz dispersa aleatoria
    B = sparse_random(n, n, density=0.5, format='csc').A
    C = A.dot(B)  # Multiplicación de matrices dispersas
    return C
