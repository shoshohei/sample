n, k = [int(i) for i in input().split(' ')]
S = list(input())

S_ls = []
count_dic = {}
for i in range(n-k+1):
    s = S[i:k+i]
    # print(i, k, s)
    S_ls.append(''.join(s))
    count_dic[''.join(s)] = 0

for s in S_ls:
    count_dic[s] += 1

# print(count_dic)
print(max(count_dic.values()))
out = [kv[0] for kv in count_dic.items() if kv[1] == max(count_dic.values())]
out = sorted(out)
print(' '.join(out))