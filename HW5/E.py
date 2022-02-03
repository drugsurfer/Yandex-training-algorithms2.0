'''
Thank snowborodist
https://github.com/snowborodist/ya-algorithms-training-2/blob/master/Division_B/Homework_5/E.py
'''
S = int(input())
enum = list(map(int, input().split()))
len_A = enum[0]
A = enum[1:]
enum = list(map(int, input().split()))
len_B = enum[0]
B = enum[1:]
enum = list(map(int, input().split()))
len_C = enum[0]
C = enum[1:]
hash_C = {}
flag = False
for i in range(len_C):
    if C[i] not in hash_C:
        hash_C[C[i]] = i
for i in range(len_A):
    for j in range(len_B):
        current = S - (A[i] + B[j])
        if current in hash_C.keys():
            print(f"{i} {j} {hash_C[current]}")
            flag = True
            break
    if flag:
        break
if not flag:
    print(-1)