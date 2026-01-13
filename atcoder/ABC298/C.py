# n = int(input())
# q = int(input())

# card_to_box = [[] for _ in range(int(2*1e5+1))]
# box_in_card = [[] for _ in range(n+1)]
# # print(card_to_box, box_in_card)
# for _ in range(q):
#     ls = [int(i) for i in input().split(' ')]
#     if ls[0]==1:
#         _, i, j = ls
#         card_to_box[i].append(j)
#         box_in_card[j].append(i)
#     if ls[0]==2:
#         res = box_in_card[ls[1]]
#         res.sort()
#         # print(res)
#         res = [str(i) for i in res]
#         print(' '.join(res))
#     if ls[0]==3:
#         res = card_to_box[ls[1]]
#         res = list(set(res))
#         res.sort()
        
#         res = [str(i) for i in res]
#         print(' '.join(res))
    
import sys, bisect

n = int(input())
q = int(input())

box_in_card = [[] for _ in range(n+1)]
card_to_box = [set() for _ in range(2*10**5+1)]

for _ in range(q):
    ls = list(map(int, input().split()))
    if ls[0] == 1:
        _, i, j = ls
        bisect.insort(box_in_card[j], i)
        card_to_box[i].add(j)            
    elif ls[0] == 2:
        j = ls[1]
        print(" ".join(map(str, box_in_card[j])))
    else:
        i = ls[1]
        print(" ".join(map(str, sorted(card_to_box[i]))))
