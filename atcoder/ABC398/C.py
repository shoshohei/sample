n = int(input())
a = [int(i) for i in input().split(' ')]
dic={}
for i in a:
    dic[i]=-1
for i in a:
    dic[i]+=1
max_num=-1
for key, data in dic.items():
    if data==0 and key>max_num:
        max_num = key
if max_num in a:print(a.index(max_num)+1)
else:print(max_num)
