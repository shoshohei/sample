n, q = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]
A.sort()
import bisect
prefix_sum = [0]*(n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i]+A[i]
sum_A = prefix_sum[-1]

for _ in range(q):
    b = int(input())
    idx = bisect.bisect_left(A, b)
    b_upper_id = n-idx
    if b_upper_id==len(A): 
        ans = b
    elif b_upper_id==0: 
        ans = -1
    else:
        temp_sum_A = 0
        temp_sum = prefix_sum[idx]
        ans = b+(b-1)*(b_upper_id-1)+temp_sum
    if ans>=sum_A: ans = -1
    print(ans)


