x, y = [int(i) for i in input().split(' ')]
count = 0
val = x
while val <= y:
    val = val*2
    count += 1

print(count)