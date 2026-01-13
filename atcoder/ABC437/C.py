import numpy as np
T = int(input())

for t in range(T):
    n = int(input())
    W, P, WP= [0]*n, [0]*n, [0]*n
    for i in range(n):
        W[i], P[i] = [int(i) for i in input().split(' ')]
        WP[i] = W[i] + P[i]
    ids = np.argsort(WP)
    sum_power = sum(P)
    res = 0
    for id, i in enumerate(ids):
        w, p = W[i], P[i]
        res += w+p
        if res>sum_power:
            print(id)
            break