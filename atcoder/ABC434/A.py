w,b = [int(i) for i in input().split(' ')]
# a = int(input())
w = w*1000

n=0
while True:
    if w<n*b:
        break
    n+=1

print(n)