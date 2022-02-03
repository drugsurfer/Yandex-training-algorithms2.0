n, q = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0] * (len(nums) + 1)
for i in range(1, len(nums) + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
for i in range(q):
    left, right = map(int, input().split())
    print(prefix_sum[right] - prefix_sum[left - 1])
