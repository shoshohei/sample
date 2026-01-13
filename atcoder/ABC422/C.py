n = int(input())

for _ in range(n):
    a,b,c = [int(i) for i in input().split(' ')]
    temp = min(min(a,c), (a+b+c)//3)
    print(temp)
