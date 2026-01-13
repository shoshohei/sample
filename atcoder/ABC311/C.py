n = int(input())
A = [int(i) for i in input().split(' ')]
from collections import defaultdict
G = defaultdict()
for id, a in enumerate(A):
    G[id+1] = a
visited = [False]*(n+1)
path = []
current = 1

while visited[current]==0:
    visited[current] = 1
    path.append(current)
    current = G[current]

out_path = []
is_cycle = False
for p in path:
    if p==current: is_cycle = True
    if is_cycle:
        out_path.append(str(p))

print(len(out_path))
print(' '.join(out_path))