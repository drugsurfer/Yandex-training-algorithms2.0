dct = {}
N = int(input())
for i in range(N):
    num = int(input())
    if num == 0:
        theme, message = input(), input()
        dct[i + 1] = [0, 1, theme]
    else:
        message = input()
        dct[i + 1] = [num]
        pointer = num
        while True:
            if dct[pointer][0] == 0:
                break
            else:
                pointer = dct[pointer][0]
        dct[pointer][1] += 1
max_cnt = 0
max_index = 0
for number in dct.keys():
    body = dct[number]
    if body[0] == 0:
        if body[1] > max_cnt:
            max_cnt = body[1]
            max_index = number
print(dct[max_index][2])

