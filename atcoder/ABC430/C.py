from bisect import bisect_left
n,a,b = [int(i) for i in input().split(' ')]
S = list(input())
num_a = [0]*(n+1)
num_b = [0]*(n+1)
i=0
for c in S:
    i+=1
    num_a[i] = num_a[i-1] + (1 if c=='a' else 0)
    num_b[i] = num_b[i-1] + (1 if c=='b' else 0)

count = 0
print(num_a, num_b)
for l in range(1, n+1):
    target_a = num_a[l-1]+a
    r_a = bisect_left(num_a, target_a, lo=1, hi=n+1)
    print(f'\t{target_a}, {r_a}')
    if r_a > n:
        continue

    target_b = num_b[l-1]+b
    r_b_fail = bisect_left(num_b, target_b, lo=1, hi=n+1)
    print(target_b, r_b_fail)
    if r_b_fail>n:
        r_b = n
    else:
        r_b = r_b_fail-1
    if r_a<=r_b:
        count += (r_b-r_a+1)
print(count)