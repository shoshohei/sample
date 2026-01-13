x, y, z = [int(i) for i in input().split(' ')]
# int(input()
out = 'No'
for i in range(100):
    if x/y==z:
        out = 'Yes'
        break
    else:
        x+=1
        y+=1
print(out)