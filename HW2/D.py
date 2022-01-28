L, K = map(int, input().split())
coord = list(map(int, input().split()))
mid = L / 2
if mid > int(mid) and int(mid) in coord:
    print(int(mid))
else:
    flag = False
    l, r = 0, 0
    for i in range(int(mid) - 1, -1, -1):
        if not flag and i in coord:
            flag = True
            l = i
            break
    flag = False
    for i in range(int(mid), L):
        if not flag and i in coord:
            flag = True
            r = i
            break
    print(l, r)