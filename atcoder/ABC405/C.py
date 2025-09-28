n = int(input())
a = [int(i) for i in input().split(' ')]
s = []
sum=0
for i in range(n):
    sum+=a[n-i-1]
    s.append(sum)
res = 0
for i in range(n-1):
    res += a[i]*s[n-2-i]
print(res)
