n, x, y = [int(i) for i in input().split(' ')]
C,A,B = [0]*n, [0]*n, [0]*n
for i in range(n): C[i],A[i], B[i] = [int(i) for i in input().split(' ')]

graph_range = sum(B)
graph_dic = {}
for i in range(-1*graph_range-1, )