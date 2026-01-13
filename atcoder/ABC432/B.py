ls = [int(i) for i in list(input())]
bool_ls = [False]*(len(ls))
for id, i in enumerate(ls):
    if i==0:
        bool_ls[id] = True

if sum(bool_ls)==0:
    ls.sort()
    ls = [str(i) for i in ls]
    print(''.join(ls))
else:
    nonzoro_ls = [i for i in ls if i!=0]
    nonzoro_ls.sort()
    min_val = nonzoro_ls[0]
    res = [min_val]
    res.extend([0]*(len(ls)-len(nonzoro_ls)))
    if len(nonzoro_ls[1:])!=0: res.extend(nonzoro_ls[1:])
    res = [str(i) for i in res]
    print(''.join(res))
