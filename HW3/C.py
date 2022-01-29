nums = list(map(int, input().split()))
elements = set()
result = []
for i in range(len(nums)):
    if nums[i] not in elements:
        elements.add(nums[i])
        result.append(nums[i])
    else:
        if nums[i] in result:
            result.remove(nums[i])
print(*result)