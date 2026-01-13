a, b, c = [int(i) for i in input().split(' ')]
ls = [a,b,c]
ls.sort()
print(100*ls[2]+10*ls[1]+ls[0])