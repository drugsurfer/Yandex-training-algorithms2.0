dct = {}
with open("input.txt") as file:
    for line in file:
        canditate, votes = line.split()
        if canditate not in dct:
            dct[canditate] = 0
        dct[canditate] += int(votes)
sortcanditate = sorted(dct.keys())
for i in sortcanditate:
    print(i, dct[i])
