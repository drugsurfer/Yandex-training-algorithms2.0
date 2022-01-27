N, i, j = map(int, input().split())
if i > j: i, j = j, i
first_way = list(range(i - 1, 0, -1)) + list(range(N, j, -1))
second_way = list(range(i + 1, j))
if len(first_way) > len(second_way):
    print(len(second_way))
else:
    print(len(first_way))