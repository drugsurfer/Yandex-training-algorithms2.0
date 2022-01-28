text = input()
count = 0
for i in range(len(text) // 2):
    if text[i] != text[len(text) - i - 1]:
        count += 1
print(count)