dct = {}
with open("input.txt") as file:
    for line in file:
        words = line.split()
        for word in words:
            if word not in dct:
                dct[word] = 0
            dct[word] -= 1
res = []
for i in dct.keys():
    res.append((dct[i], i))
result = sorted(res)
for i in range(len(result)):
    print(result[i][1])
