import numpy as np
n = int(input())
T= [int(i) for i in input().split(' ')]
T_id = np.argsort(T)
print(f'{T_id[0]+1} {T_id[1]+1} {T_id[2]+1}')