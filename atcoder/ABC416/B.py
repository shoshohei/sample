def a(s, l, r, c):
    out = True
    for i in range(l, r+1):
        if s[i]!=c:
            out = False
            break
    return out


s = input()
s = list(s)
t = s.copy()
for id, c in enumerate(t):
    if c=='.':
        t[id]='o'
        
end = len(s)
i = 0

if a(t, 0, end-1, 'o'):
    t = s
    i = end*2
    t[0] = 'o'

while i<end:
    if i!=end:
        if t[i]=='o' and i!= end-1:
            tale =0
            while i + tale < len(t) and a(t, i, i+tale, 'o'):
                tale +=1
            tale -= 1
            for j in range(i+1, i+tale+1):
                t[j] = '.'
            i += tale+1
        else: i+=1


t = ''.join(t)


print(t)

