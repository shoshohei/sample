import numpy as np
n = int(input())
p = [int(i) for i in input().split(' ')]
rank_idx = np.argsort(p)
rank_idx = [rank_idx[len(rank_idx)-1-i] for i in range(len(rank_idx))]
rank_p = [p[i] for i in rank_idx]
pre= 0
res = []
r = 1
for id, i in enumerate(rank_p):
    if pre == i:res.append(r)
    else:
        res.append(id+1)
        r = id+1
    pre = i
dis = [0]*len(p)
for i, re in zip(rank_idx, res):
    dis[i] = re
for i in dis:
    print(i)