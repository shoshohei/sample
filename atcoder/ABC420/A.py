x, y = [int(i) for i in input().split(' ')]

temp = x+y
if temp >=13:
    temp -= 12

print(temp)