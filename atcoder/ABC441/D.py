N, M, L, S, T= [int(i) for i in input().split(' ')]
U, V, C = [0]*N, [0]*N, [0]*N
for i in range(M):
    U[i], V[i], C[i] = [int(i) for i in input().split(' ')]

G = [[0]*(N+1) for _ in range(N+1)]
for u,v,c in zip(U,V,C):
    G[u][v] = C
from collections import deque
max_depth = L
start = 1
q = []
# def bfs():
#     costs = [-1]*N
#     q = deque()
#     costs[start] = 0
#     q.append(start)
#     count = 0
#     while q and count<max_depth:
#         v = q.popleft()
#         for nv in G[v]:
#             costs[nv] = costs[v]+G[v][nv]
#             q.append(nv) 
#         count += 1
def dfs(v):
    for nv in G[v]:
        