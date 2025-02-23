import numpy as np
n = int(input())
ls_s = []
for _ in range(n):
    ls_s.append(input())
ls_len= []
for s in ls_s:
    ls_len.append(len(s))
indexes = np.argsort(np.array(ls_len))
s = ''
for index in indexes:
    s += ls_s[index]
print(s)