def upper_count_num(first, last):
    first_s = str(first)
    n = len(first_s)
    print(first_s[:-1], n)
    count = 0
    for id, s in enumerate(first_s):
        # print(s)
        if s=='9':
            continue
        count += (9-int(s))*int(s)**(n-id-1)
        print(count)
    
    return count

def below_count_num(first, last):
    a = upper_count_num(first+1, first*10)
    b = upper_count_num(last, first*10)
    print(a,b)
    return b-a

start, end = [int(i)for i in input().split(' ')]
keta = 10
answer = 0
while(keta<end):
    if start > keta: 
        keta*=10
        continue
    answer += upper_count_num(start, keta) 
    keta*=10
answer += below_count_num(keta//10, end)
print(answer)
# print(count_num(81, 100))