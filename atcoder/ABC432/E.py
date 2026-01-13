n, q = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]
Q, V1, V2 = [0]*n, [0]*n, [0]*n
for i in range(n): Q[i], V1[i],V2[i] =  [int(i) for i in input().split(' ')]
q_2 = sum(Q)-q
prefix_ls = [[0]*(n+1) for _ in range(q_2)]
for id, ls in enumerate(prefix_ls):
    for i in range(len(ls)):
        prefix_ls[id][i+1] = prefix_ls[id][i] + max()