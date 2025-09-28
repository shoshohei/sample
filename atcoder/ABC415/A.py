n = int(input())
a = [int(i) for i in input().split(' ')]
x = int(input())

flg = 'No'

for i in a:
    if i==x:
        flg = 'Yes'

print(flg)