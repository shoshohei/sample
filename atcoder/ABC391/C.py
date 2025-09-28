[n, q] = [int(i) for i in input().split(' ')]
bird_from_nest = {}
nest_from_bird = {}
birds_nest_ = 0
for i in range(1, n+1): 
    bird_from_nest[i]=[i] # 巣から鳩を
    nest_from_bird[i]=i # 鳩から巣を
for i in range(q):
    ls = [int(i) for i in input().split(' ')]
    if ls[0]==1:
        bird_from_nest[ls[2]].append(ls[1])
        bird_from_nest[nest_from_bird[ls[1]]].remove(ls[1])
        if len(bird_from_nest[nest_from_bird[ls[1]]])==1: birds_nest_-=1
        if len(bird_from_nest[ls[2]])==2: birds_nest_+=1
        nest_from_bird[ls[1]] = ls[2]
    else:
        print(birds_nest_)