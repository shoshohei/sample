a = int(input())
n = int(input())

import numpy as np
def base_n(val_10, b):
    return np.base_repr(val_10, b)

ls = set()
sum = 0
for i in range(1, 10**6+1):
    x = str(i)
    rx = x[::-1]
    ls.add(int(x+rx))
    ls.add(int(x+rx[1:]))

for x in ls:
    if x>n:continue
    v = base_n(x, a)
    
    if v==v[::-1]: sum += x

print(sum)