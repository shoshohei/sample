n = int(input())
A = [int(i) for i in input().split(' ')]

dp = {}
ans = 0
for a in A:
    dp[a] = dp.get(a-1, 0) + 1
    ans = max(ans, dp[a])

print(ans)

m, a, b = [int(i) for i in input().split(' ')]

for i in  range(1, m):
    for j in range(1, m):
        x, y = i, j
        