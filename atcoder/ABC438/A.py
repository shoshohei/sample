# n = int(input())
d, f = [int(i) for i in input().split(' ')]
count = 0
count += f
while count<=d:
    count+= 7
print(count-d)