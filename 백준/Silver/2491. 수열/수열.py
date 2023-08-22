N = int(input())
lst = list(map(int, input().split()))
up = [1]
down = [1]
for i in range(1, N):
    if lst[i] <= lst[i-1]:
        down.append(down[i-1]+1)
    else:
        down.append(1)
    if lst[i] >= lst[i-1]:
        up.append(up[i-1]+1)
    else:
        up.append(1)
print(max(max(up), max(down)))