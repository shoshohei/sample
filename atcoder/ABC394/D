def check(i, j):
    if _s[i-j]=='(' and _s[i+j+1]==')':
        return True
    elif _s[i-j]=='[' and _s[i+j+1]==']':
        return True
    elif _s[i-j]=='<' and _s[i+j+1]=='>':
        return True
    else: return False

s=input()
_s=list(s)
start=0
fin=len(s)
items = ['<>', '[]', '()']
i=0
while i<fin:
    if 