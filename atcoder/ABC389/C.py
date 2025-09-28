q = int(input())
head_ls = []
teal_ls = []
start = geta = 0
for i in range(q):
    q_ = [int(i) for i in input().split(' ')]
    if q_[0]==1:
        if len(head_ls)==0:
            head_ls.append(0)
            teal_ls.append(q_[1])
        else:
            head_ls.append(teal_ls[-1])
            teal_ls.append(head_ls[-1]+q_[1])
    elif q_[0]==2:
        # a = teal_ls[0]
        # teal_ls = teal_ls[1:]
        # head_ls = head_ls[1:]
        # head_ls = [i-a for i in head_ls]
        # teal_ls = [i-a for i in teal_ls]
        geta += teal_ls[start]
        start += 1
    elif q_[0]==3:
        id = start + q_[1]-1
        print(head_ls[id]-geta)
    # print(head_ls, teal_ls, start, geta)