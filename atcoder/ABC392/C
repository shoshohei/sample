import numpy as np
n = int(input())
p = [int(i) for i in input().split(' ')]
q = [int(i) for i in input().split(' ')]
sorted_indices = np.argsort(q)
res = []
for id, i in enumerate(sorted_indices):
    res.append(str(q[p[i]-1]))
print(' '.join(res))
