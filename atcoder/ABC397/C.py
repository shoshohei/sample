n = int(input())
a = [int(i) for i in input().split(' ')]

left = set([])
right = set([])
numl = []
numr = []
for i in range(n-1):
    left.add(a[i])
    right.add(a[n-1-i])
    numl.append(len(left))
    numr.append(len(right))
# print(numl, numr)
ans = 0
for i in range(n-1):
    ans = max(ans, numl[i]+numr[n-2-i])
print(ans)