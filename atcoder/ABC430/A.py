a,b,c,d = [int(i) for i in input().split(' ')]
out = 'No'

if c>=a:
    if d>=b:
        out = 'No'
    else:
        out = 'Yes'

print(out)