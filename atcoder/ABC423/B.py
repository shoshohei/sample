n = int(input())
isLock = [int(i) for i in input().split(' ')]
start_lock = -1
ans = 0
for id, i in enumerate(isLock):
    if i==1:
        start_lock = id+2
        break

end_lock = n+2
re_isLock = list(reversed(isLock))
for id, i in enumerate(re_isLock):
    if i==1:
        end_lock = n-id
        break
# print(end_lock, start_lock, ans)
ans += (end_lock - start_lock+1)
if ans<=0: ans = 0
if sum(isLock)==0: ans = 0
print(ans)
