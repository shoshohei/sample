n = int(input())
ls = []
sum = 0
for _ in range(n):
    c, l = [i for i in input().split(' ')]
    l = int(l)
    sum += l
    if sum>100: 
        ls = None
        break
    for _ in range(l): ls.append(c)

if ls != None: print(''.join(ls))
else: print('Too Long')