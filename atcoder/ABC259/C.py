S = list(input())
T = list(input())

def rle(s):
    vec = []
    cnt = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            vec.append((s[i - 1], cnt))
            cnt = 0
        cnt += 1
    vec.append((s[-1], cnt))
    return vec

s_vec = rle(S)
t_vec = rle(T)

if len(s_vec)!=len(t_vec):
    out = 'No'
else:
    out = 'Yes'
    for (schar, snum), (tchar, tnum) in zip(s_vec, t_vec):
        if schar!=tchar: 
            out = 'No'
            break
        if not (snum==tnum or (snum<tnum and snum>=2)):
            out = 'No'
            break
print(out)