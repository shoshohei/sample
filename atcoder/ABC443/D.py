T = int(input())
N = [0]*T
RR = []
for i in range(T):
    N[i] = int(input())
    R = [int(j) for j in input().split(' ')]
    RR.append(R)
import numpy as np
for t in range(T):
    n, R = N[t], RR[t]
    count = 0
    maxid_R = np.argmin(R)
    max_R = np.min(R)
    left_val = max_R
    # print(max_R, maxid_R)
    for i in range(1, maxid_R+1):
        id = maxid_R - i
        if left_val>R[id]:
            if abs(left_val-R[id])>1:
                count += left_val-R[id]-1
            left_val = R[id]
            
        else:

            if abs(left_val-R[id])>1:
                count += abs(left_val+1-R[id])
                # print(abs(left_val+1-R[id]))
                left_val = R[id]-abs(left_val+1-R[id])
            
            else:
                left_val = R[id]
    right_val = max_R
    # print(f'left={count}')
    for i in range(n-maxid_R-1):
        id = maxid_R+1+i
        if right_val>R[id]:
            if abs(right_val-R[id])>1:
                count += abs(right_val-R[id]-1)
            right_val = R[id]
        else:  
            if abs(right_val-R[id])>1:
                count += abs(right_val+1-R[id])
                # print(abs(right_val+1-R[id]))
                right_val = R[id]-abs(right_val+1-R[id])
            else:
                right_val = R[id]
            
        # print(id, right_val, count, R[id])
    print(count)