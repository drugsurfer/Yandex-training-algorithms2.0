i, j, year = list(map(int, input().split()))
if i == j: print(1)
elif i <= 12 and j <= 12:
    print(0)
else: print(1)