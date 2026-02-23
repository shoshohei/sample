T = int(input())

for t in range(T):
    n, d = [int(i) for i in input().split(' ')]
    A = [int(i) for i in input().split(' ')]
    B = [int(i) for i in input().split(' ')]
    eggNum = 0
    used = 0
    dayLim = [0]*(n+1)
    for i in range(1, n+1):
        eggNum += A[i-1]
        used += B[i-1]
        dayLim[i] += A[i-1]
        if i-d>0:
            used = dayLim[i-d]
    print(eggNum-used)
