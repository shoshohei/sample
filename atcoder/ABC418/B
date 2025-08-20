s = list(input())

pos_t = []
for id, c in enumerate(s):
    if c=='t': pos_t.append(id)
if len(pos_t)<2: 
    # print('in/')
    print('0')
else:
    s = s[pos_t[0]:pos_t[-1]+1]
    pos_t = [val-pos_t[0] for val in pos_t]
    if len(s)<3: print('0')
    else:
        ans= []
        # print(s, pos_t)
        for i in pos_t:
            for j in pos_t:
                if j-i>=2:
                    count = 0
                    temp_s = s[i:j+1]
                    for id, c in enumerate(temp_s):
                        if c=='t': count+=1
                    ans.append((count-2)/(j-i-1))
                    # print(s[i:j+1])
        # print(ans)
        print('{:.20f}'.format(max(ans)))