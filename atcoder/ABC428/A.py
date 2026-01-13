s, a, b, x = [int(i) for i in input().split(' ')]
sum_t = 0
dis = 0
while sum_t<=x:
    if sum_t+a>x:
        dis += s*(x-sum_t)
    else:
        dis += s*a
    sum_t += (a+b)
print(dis)