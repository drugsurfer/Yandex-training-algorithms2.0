n = int(input())
dct = {}
for _ in range(n):
    d, a = map(int, input().split())
    if d not in dct:
        dct[d] = 0
    dct[d] += a
sortcolor = sorted(dct.keys())
for i in sortcolor:
    print(i, dct[i])