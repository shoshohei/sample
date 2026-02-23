N, K, X= [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]

A.sort()

sel = N
sumMinK = sum(A[:K])
sake = sumMinK
sum_ = sum(A)
while sum_>=X and sel-K>=0:
    sum_ = sake + sum(A[K:sel])
    sel-=1

if sel-K<0:print(-1)
else:print(sel)
