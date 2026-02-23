p, q= [int(i) for i in input().split(' ')]
x, y= [int(i) for i in input().split(' ')]
if x <= p+99 and y <= q+99 and x>=p and y>=q: print('Yes')
else:
    print('No')