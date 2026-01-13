N, M = [int(i) for i in input().split(' ')]
X, Y = [0]*M, [0]*M
for i in range(M):
    X[i], Y[i] = [int(i) for i in input().split(' ')]
from collections import defaultdict
Q = int(input())
G = [defaultdict() for _ in range(N)]
for i in range(M):
    G[X[i]].append(Y[i])
reverse_G = [defaultdict() for _ in range(N)]
for i in range(M):
    reverse_G[Y[i]].append(X[i])

Op, Val = [0]*(Q), [0]*Q
for i in range(M):
    Op[i], Val[i] = [int(i) for i in input().split(' ')]

bool_Node = [False]*(N+1)

for i in range(Q):
    op, val = Op[i], Val[i]
    if op==1:
        bool_Node[val] = True
        q = reverse_G[val]
        while q:
            node = q.pop()
            