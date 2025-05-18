[n, k] = [int(n) for n in input().split(' ')]
a = [1 for _ in range(k)]
s = [i for i in range(k+1)]
for i in range(k, n+1):
    a.append((s[i]-s[i-k])%10e8)
    s.append((s[i]+a[i])%10e8)
print(a, s)
print(int(a[-1]))
