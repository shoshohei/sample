n, q = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]

for i in range(n):
    A.append(A[i])
first = 0
sum_A = [0]*(2*n+1)
for i in range(2*n):
    sum_A[i+1] = sum_A[i]+A[i]
# print(sum_A)
for i in range(q):
    ls = [int(i) for i in input().split(' ')]
    if ls[0]==1:
        first += ls[1]
        if first > n:
            first -= n
    else:
        _, l, r = ls
        l += first
        # if l>n: l -= first
        r += first
        # if r>n: r -= first
        # print(f'{l}:{r}:{first}\n')
        # print(sum_A[r],sum_A[l-1])
        sum = sum_A[r]-sum_A[l-1]
        print(sum)
        