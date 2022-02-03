enum = input()
dct = {'(' : 1, ')' : -1}
prefix_sum = 0
for sym in enum:
    prefix_sum += dct[sym]
    if prefix_sum < 0:
        break
if prefix_sum == 0:
    print('YES')
else:
    print('NO')