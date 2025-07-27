t = int(input())

for _ in range(t):
    res = 'Yes'
    num = int(input())
    s = input()
    # pos = [i for i, c in enumerate(s) if c == '1']
    # # 危険になる状態の二進数表記
    # bins = [format(p+1, 'b') for p in pos]
    # for b in bins:

    # 全部入れたらアウトか確認
    if s[-1]=='1': res = 'No'

    # 一種類入れた場合がすべてダメか確認
    if res!='No':
        boo = [False]*num
        for i in range(num):
            if s[2**i-1]=='1':
                boo[i] = True
        if sum(boo)==num: res = 'No'

    if res!='No':
        

    


    print(res)