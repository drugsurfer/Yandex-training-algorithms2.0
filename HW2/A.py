hash = {}
num = int(input())
while num != 0:
    if num not in hash:
        hash[num] = 0
    hash[num] += 1
    num = int(input())
print(hash[max(hash.keys())])