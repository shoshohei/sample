x, y = [i for i in input().split(' ')]
out = 'Yes'
x_num, y_num = -1, -1
if x=='Ocelet':
    x_num = 0
elif x=='Serval':
    x_num = 1
elif x=='Lynx':
    x_num = 2
if y=='Ocelet':
    y_num = 0
elif y=='Serval':
    y_num = 1
elif y=='Lynx':
    y_num = 2

if x_num>=y_num:print('Yes')
else: print('No')