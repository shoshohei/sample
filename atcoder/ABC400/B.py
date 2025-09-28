[n, m] = [int(i) for i in input().split(' ')]
ans = 0
for i in range(m+1):
    ans+=n**i
    if ans >1e9:
        ans='inf'
        break
print(ans)