n, m = [int(i) for i in input().split(' ')]
s = list(input())
t = list(input())

num_swap = [0]*(n+1)

for i in range(m):
    l, r = [int(i) for i in input().split(' ')]
    num_swap[l-1] ^= 1
    num_swap[r] ^= 1
cur = 0
for i in range(n):
    cur ^= num_swap[i]
    if cur==1:
        s[i] = t[i]
print(''.join(s))
