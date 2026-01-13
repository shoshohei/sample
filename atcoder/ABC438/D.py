n = int(input())
A = [int(i) for i in input().split(' ')]
B = [int(i) for i in input().split(' ')]
C = [int(i) for i in input().split(' ')]

prefix_A = [0]*(n+1)
prefix_B = [0]*(n+1)
prefix_C = [0]*(n+1)
for i in range(n):
    prefix_A[i+1] = prefix_A[i]+A[i]
    prefix_B[i+1] = prefix_B[i]+B[i]
    prefix_C[i+1] = prefix_C[i]+C[i]

ans = -10**18
best = prefix_A[1] - prefix_B[1]

for j in range(2, n):
    best = max(best, prefix_A[j-1] - prefix_B[j-1])
    cur = prefix_C[n] + best + (prefix_B[j] - prefix_C[j])
    ans = max(ans, cur)

print(ans)