n, m = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]
B = [int(i) for i in input().split(' ')]
import bisect
A.sort()
B.sort()
prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i]+A[i]
num = 998244353
val = [0]*m
for i in range(m):
    pos = bisect.bisect(A, B[i])
    
    # val[i] += (pos*B[i] - sum(A[:pos]))%num
    # val[i] += (sum(A[pos:]) - (n-pos)*B[i])%num
    # print(i, sum(A[:pos]), sum(A[pos:]))
    # val[i] = val[i]%num
    val[i] += (pos*B[i] - prefix[pos])%num
    val[i] += (prefix[-1]-prefix[pos] - (n-pos)*B[i])%num
    val[i] = val[i]%num
    # print(i, sum(A[:pos]), sum(A[pos:]), prefix[pos], prefix[-1]-prefix[pos])
    # print(pos, val[i])

print(sum(val)%num)