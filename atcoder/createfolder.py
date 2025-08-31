import os 
from pathlib import Path

num = 421
file_names = ['A', 'B', 'C', 'D']

for i in range(1, num+1):
    str_i = str(i)
    if len(str_i)==1:
        str_i = '00'+str_i
    elif len(str_i)==2:
        str_i = '0'+str_i

    dir_path = './atcoder/ABC'+str_i+'/'
    os.makedirs(dir_path, exist_ok=True)
    for j in file_names:
        Path(dir_path+j+'.py').touch(exist_ok=True)

