n = int(input())
a = [int(i) for i in input().split(' ')]
count = 0

diff_j = [j-a[j] for j in range(n)]
l = (max(diff_j)+1)
dic = [0]*l
for dif in diff_j:
    if dif >0: dic[dif]+=1 

for i in range(n):
    sum_i = i+a[i]
    if sum_i<l: count += dic[sum_i]
print(count)