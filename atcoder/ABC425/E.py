T, mod = map(int, input().split())

K = 5001

binom = [[0] * K for i in range(K)]
binom[0][0] = 1

for n in range(1, K):
    binom[n][0] = 1
    for k in range(1, n + 1):
        binom[n][k] = (binom[n - 1][k - 1] + binom[n - 1][k]) % mod

for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    ans = 1
    s = 0
    for i in C:
        s += i
        ans *= binom[s][i]
        ans %= mod
    print(ans % mod)
