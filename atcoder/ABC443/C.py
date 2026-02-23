n, T = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]

ans = 0
isLook = True
next = 0
last = 0

for a in A:
    if isLook:
        ans += 