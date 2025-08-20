n = int(input())
pos_x = []
pos_y = []

for i in range(n):
    x, y = [int(i) for i in input().split(' ')]
    pos_x.append(x)
    pos_y.append(y)

import numpy as np 

center_x = (max(pos_x)+min(pos_x))/2
center_y = (max(pos_y)+min(pos_y))/2

# print(center_x, center_y)
serch_pos = [[int(center_x), int(center_y)], [int(center_x+0.5), int(center_y)], [int(center_x), int(center_y+0.5)], [int(center_x+0.5), int(center_y+0.5)]]
# print(serch_pos)
max_dis = []
for t in serch_pos:
    x_, y_ = t
    diff_x = [np.abs(x_-x) for x in pos_x]
    diff_y = [np.abs(y_-y) for y in pos_y]
    max_dis.append(max(max(diff_x), max(diff_y)))
# print(max_dis)
print(min(max_dis))