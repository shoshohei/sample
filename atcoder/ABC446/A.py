# h, w = [int(i) for i in input().split(' ')]
# S = [[] for i in range(h)]
# for i in range(h):
#     S[i] = list(input())
def inRange(start, end, val):
    if val>=start and val<=end: return True
    return False
import math
n = int(input())
min_id = -1
L, R, diff = [0]*n, [0]*n, [0]*n 
for j in range(n): 
    L[j], R[j] = [int(i) for i in input().split(' ')]
    diff[j] = R[j]-L[j]
min_id = min(range(len(diff)), key=lambda i: diff[i])
ans = 0
for i in range(L[min_id], R[min_id]+1):
    if i == 1: ans += 1
    else:
        cnt = 0
        for id in range(n):
            if min_id==id: continue
            if inRange(L[id], R[id], i):
                cnt += 1
        # print(i, math.comb(cnt, i-1), cnt)
        ans += math.comb(cnt, i-1)

print(ans*2)