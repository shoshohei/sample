n, m = [int(i) for i in input().split(' ')]
L = [0]*n
cans = [False]*(m+1) 
Xs = []
for i in range(n): 
    L[i] = int(input())
    X = [int(i) for i in input().split(' ')]
    Xs.append(X)

isExist = [False]*n 
for i in range(n):
    for x in Xs[i]:
        if not cans[x]:
            print(x)
            cans[x] = True
            isExist[i] = True
            break
    if not isExist[i]: 
        print(0)