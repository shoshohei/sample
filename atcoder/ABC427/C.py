# n, m = [int(i) for i in input().split(' ')]
# # U, V = []*(m), []*(m)
# U, V = [], []
# G = [[] for i in range(n)]
# for i in range(m):
#     u, v = [int(i) for i in input().split(' ')]
#     u-=1
#     v-=1
#     U.append(u)
#     V.append(v)
#     G[u].append(v)
#     G[v].append(u)
# from collections import deque
# count_ls = []
# for num in range(n):
#     Colors = ['']*(n)
#     Colors[num] = 'w'
#     # current = 0
#     visited = [False]*n
#     visited[num] = True
#     q = deque([num])
#     while q:
#         current = q.popleft()
#         for node in G[current]:
#             if Colors[node]=='':
#                 if Colors[current]=='w': Colors[node] = 'b'
#                 else: Colors[node] = 'w'
#                 q.append(node)
#                 visited[node] = True
#                 # print(node, Colors,q)
            

#     count = 0
#     for u, v in zip(U, V):
#         if Colors[u]==Colors[v]:
#             count+=1
#     # print(count)
#     count_ls.append(count)
# print(min(count_ls))

import sys

n, m = [int(i) for i in input().split(' ')]
edges = []
for _ in range(m):
    u, v = [int(i) for i in input().split(' ')]
    u-=1
    v-=1
    edges.append((u, v))

max_cut = 0
for mask in range(1<<n):
    cut = 0
    for u, v in edges:
        if ((mask >> u) & 1) != ((mask >> v) & 1):
            cut += 1
    if cut > max_cut:
        max_cut = cut

ans = m - max_cut
print(ans)
