import sys
import numpy as np
import time

def matrixmult (A, B):
    n = len(A[0])

    C = [[0 for row in range(n)] for col in range(n)]

    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

start_time = time.time()

A = [[2 for row in range(500)] for col in range(500)]
B = [[2 for row in range(500)] for col in range(500)]

C = matrixmult(A, B)

print("--- %s seconds ---" % (time.time() - start_time))
