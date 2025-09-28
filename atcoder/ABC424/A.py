h, w, n = [int(i) for i in input().split(' ')]
Z = [[0]*w for _ in range(h)]

for i in range(n):
    a, b, c, d = [int(i) for i in input().split(' ')]
    Z[a-1][b-1] = 1
    Z[c-1][d-1] = -1
    
num = 0
for i in range(h):
    out = []
    for j in range(w):
        num += Z[i][j]
        out.append(num)