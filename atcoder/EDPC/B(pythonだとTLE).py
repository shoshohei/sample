n, k = [int(i) for i in input().split(' ')]
H = [int(i) for i in input().split(' ')]

sum_H = sum(H)
dp = [sum_H+1]*(n+1)
dp[1] = 0

for i in range(1, n+1):
    for j in range(1, k+1):
        if i<n-j+1:
            val = dp[i]+abs(H[i-1]-H[i+j-1])
            if dp[i+j]>val:
                dp[i+j] = val
print(dp[-1])