n =  int(input())

A = [int(i) for i in input().split(' ')]

for i in range(n):
    # print(i)
    out = -1
    t=i-1
    if t<0: 
        out = -1
        print(out)
        continue
    else:
        for j in range(t+1):
            k = t-j
            if k <0: 
                out = -1
                print(out)
                continue
            else:
                if A[i]<A[k]:
                    out = k+1
                    break
    print(out)