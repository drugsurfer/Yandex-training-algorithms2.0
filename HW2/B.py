street = list(map(int, input().split()))
distance_A = [0 for i in range(len(street))]
distance_B = [0 for i in range(len(street))]
shop_index = -20
for i in range(len(street)):
    if street[i] == 2:
        shop_index = i
    elif street[i] == 1:
        distance_A[i] = i - shop_index
shop_index = 20
for i in range(len(street) - 1, -1, -1):
    if street[i] == 2:
        shop_index = i
    elif street[i] == 1:
        distance_B[i] = shop_index - i
max_distance = 0
for i in range(len(street)):
    if min(distance_A[i], distance_B[i]) > max_distance:
        max_distance = min(distance_A[i], distance_B[i])
print(max_distance)
