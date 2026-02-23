n, m = [int(i) for i in input().split(' ')]
A, B = [0]*m, [0]*m
G = [0]*(n+1)
for i in range(m):
    a, b = [int(i) for i in input().split(' ')]
    G[a] += 1
    G[b] += 1

out_ls = []
for i in range(1, n+1):
    num = n-1-G[i]
    if num<3:
        out_ls.append(0)
    else:
        val = int(num*(num-1)*(num-2)/6)
        out_ls.append(val)
out_ls = [str(i) for i in out_ls]
print(' '.join(out_ls))