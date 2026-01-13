S = list(input())
num_S = [int(i) for i in S]
zip_val, zip_num = [], [0]*(len(num_S)+1)
index= 0
for id, i in enumerate(num_S):
    if id==0: 
        zip_val.append(i)
    elif i!=num_S[id-1]:
        zip_val.append(i)
        index += 1
    zip_num[index] += 1
# print(zip_num, zip_val)
count = 0
for i in range(len(zip_val)-1):
    if zip_val[i]+1==zip_val[i+1]:
        count += min(zip_num[i], zip_num[i+1])
print(count)