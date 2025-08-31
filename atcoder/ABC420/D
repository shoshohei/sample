h, w = [int(i) for i in input().split(' ')]
from collections import deque
S = [input() for i in range(h)]
door_pos = []
        
def check_out_of_Map(pos):
    if pos[0] <0 or pos[0] >w:
        return False
    if pos[1] < 0 or pos[1] > h:
        return False
    return True

def CheckIsPass(pos):
    if S[pos[0]][pos[1]]=='o' or S[pos[0]][pos[1]]=='?' or S[pos[0]][pos[1]]=='G':
        return True
    return False

ukv = [[]*(w*h)]
for i in range(w):
    for j in range(h):
        # 場所の記録
        if S[i, j] == 'S': start_pos = [i, j]
        elif S[i, j] == 'G': goal_pos = [i, j]
        elif S[i, j] == 'o' or S[i, j] == 'x': door_pos.append([i, j])

        # 移動可能な場所の記録
        if ~check_out_of_Map([i,j-1]) and CheckIsPass([i, j-1]):
            ukv[i*w+h].append([i,j-1])
        if ~check_out_of_Map([i-1, j]) and CheckIsPass([i-1, j]):
            ukv[i*w+h].append([i-1, j])
        if ~check_out_of_Map([i,j+1]) and CheckIsPass([i, j+1]):
            ukv[i*w+h].append([i,j+1])
        if ~check_out_of_Map([i+1, j+1]) and CheckIsPass([i+1, j+1]):
            ukv[i*w+j].append([i+1, j+1])
            





for i in range(w):
    for j in range(h):
        


q = deque()
q.append(start_pos)
pass_count = [-1]*(h*w)

while len(q)>0:
    current_pos = q.popleft()

    for i in range(ukv[current_pos[0]*w+current_pos[1]]):
        node = ukv[current_pos[0]*w+current_pos[1]][i]
        if pass_count[node[0]*w+node[1]] == -1:
            q.append(node)
            pass_count[node[0]*w+node[1]] = pass_count = [current_pos]+1 

print(min(pass_count))