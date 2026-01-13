n, m, c = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]
ls = [0]*(m)
for i in A:
    ls[i]+=1
ls.extend(ls)
sum_all = 0

sum_0 = 0
sum_id_last = -1
for id, i in enumerate(ls[1:]):
    if sum_0>=c: break
    sum_0 += i
    sum_id_last = id+1
print(sum_0, sum_id_last)
print(ls)
sum_all += sum_0
for i in range(1,m):
    print(f'in{sum_all}')
    sum_0 -= ls[i-1]
    if sum_0<0: sum_0 = 0
    print(f'if{sum_0}')
    if sum_0>=c: 
        sum_all += sum_0
        sum_id_last += 1
        continue
    
    for id, j in enumerate(ls[sum_id_last+1:]):
        print(id+sum_id_last+1, j, sum_0)
        if sum_0>=c: break
        sum_0 += j
        sum_id_last = id+sum_id_last+2
    sum_all += sum_0

print(sum_all)