x = int(input())
n = int(input())
W = [int(i) for i in input().split(' ')]
Q = int(input())
parts = [False]*(n+1)

weight = x
for i in range(Q):
    p = int(input())
    parts[p] = ~parts[p]
    if parts[p]:
        weight += W[p-1]
    else: weight -= W[p-1]
    print(weight)
