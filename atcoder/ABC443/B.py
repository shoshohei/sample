n, k = [int(i) for i in input().split(' ')]
accum = 0
count = 0

while accum<k:
    accum += count+n
    count+=1

print(count-1)