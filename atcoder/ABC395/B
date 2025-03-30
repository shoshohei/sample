n = int(input())
ar =  [['0'] * n for _ in range(n)]
if n%2!=0: a, b='#', '.'
else: a, b='.', '#'
for i in range((n+1)//2):
    for j in range(0, i):
            if j%2==0:
                ar[i][j] = '#'
            else:
                ar[i][j] = '.'
    for j in range(n-i, n):
        if j%2==0:
            ar[i][j] = a
        else:
            ar[i][j] = b
    
    for j in range(i, n-i):
        if(i%2==0): ar[i][j] = '#'
        else: ar[i][j] = '.'
    

for i in range((n+1)//2):
    res = ''
    for j in range(n):
        res+=ar[i][j]
    print(res)
for i in range(0, n//2):
    res = ''
    for j in range(n):
        res+=ar[(n//2-1-i)][j]
    print(res)

