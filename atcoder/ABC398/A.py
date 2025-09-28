n = int(input())
i = int(n/2)
s=list('-'*n)
if n%2==0:
    s[i-1]='='
s[i]='='
print(''.join(s))