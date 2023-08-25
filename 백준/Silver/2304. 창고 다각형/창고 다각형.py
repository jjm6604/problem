N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
size = 0
max_length = 0
for i in range(N):
    if size < lst[i][0]:
        size = lst[i][0]
    if max_length < lst[i][1]:
        max_length = lst[i][1]
MAP = [0] * (size+1)
result = [0] * (size+1)
for i in range(N):
    MAP[lst[i][0]] = lst[i][1]
max_idx = MAP.index(max_length)
for i in range(1, max_idx):
    if MAP[i] < MAP[i-1]:
        MAP[i] = MAP[i-1]
for i in range(size-1, max_idx, -1):
    if MAP[i] < MAP[i+1]:
        MAP[i] = MAP[i+1]
print(sum(MAP))