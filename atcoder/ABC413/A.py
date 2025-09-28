n, m = [int(i) for i in input().split(' ')]
a = [int(i) for i in input().split(' ')]

out = 'No'
if sum(a)<=m: out = 'Yes'
print(out)