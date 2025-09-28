n, l, r = [int(i) for i in input().split(' ')]
count = 0

for i in range(n):
    x,y = [int(i) for i in input().split(' ')]
    if x<=l and r<=y: count +=1

print(count)