n = int(input())
H = [int(i) for i in input().split(' ')]
sum_H = sum(H)
dp = [sum_H+1]*(n+1)
dp[1] = 0
for i in range(1, n+1):
    if i<n and dp[i+1]>dp[i]+abs(H[i-1]-H[i]):
        dp[i+1] = dp[i]+abs(H[i-1]-H[i])
    if i<n-1 and dp[i+2]>dp[i]+abs(H[i-1]-H[i+1]):
        dp[i+2] = dp[i]+abs(H[i-1]-H[i+1])
    # print(dp)
print(dp[-1])