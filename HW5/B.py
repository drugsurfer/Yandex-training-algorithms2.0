n = int(input())
nums = list(map(int, input().split()))
prefix_sum = 0
max_value = nums[0]
count_negative = 0
ans = 0
for i in range(len(nums)):
    max_value = max(nums[i], max_value)
    prefix_sum += nums[i]
    if nums[i] < 0:
        prefix_sum = max(prefix_sum, 0)
        count_negative += 1
    else:
        ans = max(prefix_sum, max_value, ans)
if count_negative == len(nums):
    print(max_value)
else:
    print(ans)
