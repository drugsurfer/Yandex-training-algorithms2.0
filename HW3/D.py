n = int(input())
result = set([ _ for _ in range(1, n + 1)])
text = input()
while text != "HELP":
    test = input()
    nums = set(map(int, text.split()))
    if test == "YES":
        result.intersection_update(nums)
    else:
        result.difference_update(nums)
    text = input()
print(*sorted(list(result)))




