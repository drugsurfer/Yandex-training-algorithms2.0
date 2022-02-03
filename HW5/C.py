N, M = map(int, input().split())
groups = list(map(int, input().split()))
computers = list(map(int, input().split()))
for i in range(N):
    groups[i] = (groups[i] + 1, i)
for i in range(M):
    computers[i] = (computers[i], i)
groups.sort()
computers.sort()
point_to_group, point_to_comp = 0, 0
P = 0
result = [0] * N
while point_to_group < N and point_to_comp < M:
    if groups[point_to_group][0] <= computers[point_to_comp][0]:
        P += 1
        result[groups[point_to_group][1]] = computers[point_to_comp][1] + 1
        point_to_group += 1
        point_to_comp += 1
    else:
        point_to_comp += 1
    if point_to_comp == M:
        break
print(P)
print(*result)