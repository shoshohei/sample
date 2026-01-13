s = list(input())
l = (len(s)-1)//2
S = s[:l]+s[l+1:]
print(''.join(S))