import bisect
n, q = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]
B = []
for i in range(q): B.append(int(input()))
A.sort()
prefix_A = [0]*(n+1)
for i in range(n):
    prefix_A[i+1] = prefix_A[i]+A[i]

max_A = max(A)
sum_A = sum(A)
for b in B:
    out = 0
    if b>max_A: out = -1
    # elif b==max_A: out = sum_A
    elif b==1: out = 1
    else:
        val = bisect.bisect_left(A, b)
        # print(val,prefix_A)
        if val==n-1:
            out = prefix_A[val]+b
        else:
            out = prefix_A[val]+(n-val)*(b-1)+1
    print(out)

# 二分探索のbisectの使い方
# なんとなくでできたけどもっと数式書いて理論立てた方がいい