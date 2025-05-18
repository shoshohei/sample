n = int(input())
a = [int(i) for i in input().split(' ')]
count = 0
small_moti = a[-1]/2
for i in range(n):
    if small_moti<=a[i]: continue
    for j in range(i, n):
        if a[i]*2 <= a[j]:
            # print(i, j)
            count+=1
print(count)