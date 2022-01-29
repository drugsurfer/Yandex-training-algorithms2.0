nums = list(map(int, input().split()))
temp = set()
last_len = 0
for i in range(len(nums)):
    temp.add(nums[i])
    if len(temp) > last_len:
        print("NO")
        last_len = len(temp)
    else:
        print("YES")