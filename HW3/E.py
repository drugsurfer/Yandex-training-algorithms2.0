M = int(input())
svid = [set(input()) for _ in range(M)]
N = int(input())
numbers = []
max_cnt = 0
for i in range(N):
    cnt = 0
    num = input()
    num_set = set(num)
    for s in svid:
        if s <= num_set:
           cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
    numbers.append((num, cnt))
for i in range(N):
    if numbers[i][1] == max_cnt:
        print(numbers[i][0])