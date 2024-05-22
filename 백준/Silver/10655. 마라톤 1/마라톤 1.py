N = int(input())
point = []

for i in range(N):
    a, b = map(int, input().split())
    point.append((a, b))

max_value = 0
for i in range(0, N-2):
    d = (abs(point[i][0] - point[i + 1][0]) + abs(point[i][1] - point[i + 1][1])) + (abs(point[i + 1][0] - point[i + 2][0]) + abs(point[i + 1][1] - point[i + 2][1]))
    d2 = (abs(point[i][0] - point[i + 2][0]) + abs(point[i][1] - point[i + 2][1]))
    if d - d2 > max_value:
        max_value = d - d2

distance = 0
for i in range(N-1):
    distance += (abs(point[i][0] - point[i + 1][0]) + abs(point[i][1] - point[i + 1][1]))

print(distance - max_value)