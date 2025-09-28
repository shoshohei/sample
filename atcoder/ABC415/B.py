s = input()
c = list(s)

count = 0
ls=[]
for id, i in enumerate(c):
    if i == '#':
        count+=1
        ls.append(id+1)
    if count ==2 :
        count = 0
        temp = f'{ls[0]},{ls[1]}'
        print(temp)
        ls = []