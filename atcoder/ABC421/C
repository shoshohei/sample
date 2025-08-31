# n = int(input())
# s = list(input())
# bool_s = [c=='A' for c in s]
# start_b = bool_s[0]
# ls_A = []
# ls_B = []
# for id, b in enumerate(bool_s):
#     if b: ls_A.append(id)
#     else: ls_B.append(id)
# # print(ls_A, ls_B)

# count = 0
# for i in range(len(s)):
#     check_id = len(s)-1-i
#     check_val = bool_s[check_id]
#     if i%2!=0:
#         if start_b==check_val: isCorrect = True
#         else: isCorrect = False

#     else:
#         if start_b==check_val: isCorrect = False
#         else: isCorrect = True
#     if not isCorrect:
#         val = 4*len(s)
#         if i%2!=0:
#             while val > check_id:
#                 val = ls_A.pop()
#         else:
#             while val > check_id:
#                 val = ls_B.pop()
#         print(check_id, val)
#         count += check_id -val
#         bool_s[val] = not bool_s[val]

# bool_s = [c=='A' for c in s]
# start_b = bool_s[0]
# ls_A = []
# ls_B = []
# for id, b in enumerate(bool_s):
#     if b: ls_A.append(id)
#     else: ls_B.append(id)
# count2 = 0
# for i in range(len(s)):
#     check_id = len(s)-1-i
#     check_val = bool_s[check_id]
#     if i%2!=0:
#         if start_b!=check_val: isCorrect = True
#         else: isCorrect = False

#     else:
#         if start_b!=check_val: isCorrect = False
#         else: isCorrect = True
#     if not isCorrect:
#         # print(f'check_id:{check_id}')
#         val = 4*len(s)
#         if i%2!=0:
#             while val > check_id:
#                 val = ls_B.pop()
#         else:
#             while val > check_id:
#                 val = ls_A.pop()
#         # print(check_id, val)
#         count2 += check_id -val
#         bool_s[val] = not bool_s[val]

# print(count, count2)
# print(min(count, count2))

n = int(input())
S = list(input())
count1 = 0
count2 = 0
ls_A = []
for i in range(len(S)):
    if S[i]=='A': ls_A.append(i)
for i in range(n):
    target = 2*i
    count1 += abs(target-ls_A[i])
    # print(count1, count2)
for i in range(n):
    target = 2*i+1
    count2 += abs(target-ls_A[i])
#     print(count1, count2)
# print(count1, count2)
print(min(count1, count2))