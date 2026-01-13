n = int(input())
X, Y = [0]*n, [0]*n
for i in range(n):
    X[i], Y[i] = [int(i) for i in input().split(' ')]
A = [[] for _ in range(n+1)]
A[0] = []
str_A = ['' for _ in range(n+1)]
for i in range(1, n+1):
    A[i] = A[X[i-1]] + [Y[i-1]]
    str_A[i] = ''.join([str(i) for i in A[i]])
import numpy as np
id_A = np.argsort(str_A)
id_A = [str(i) for i in id_A]
print(' '.join(id_A[1:]))