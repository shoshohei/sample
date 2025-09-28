x, c = [int(i) for i in input().split(' ')]

ans = 1000*x//(1000+c)
ans = int(ans/1000)*1000
print(ans)