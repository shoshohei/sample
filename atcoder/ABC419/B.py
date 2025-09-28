q = int(input())

ls = []
for i in range(q):
    temp = [int(i) for i in input().split(' ')]
    if temp[0]==1:
        ls.append(temp[1])
    else:
        ls.sort()
        print(ls[0])
        ls = ls[1:]