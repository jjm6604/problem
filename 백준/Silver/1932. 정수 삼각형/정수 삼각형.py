n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
for i in range(n-2, -1, -1):
    for j in range(len(lst[i])):
        value = max(lst[i+1][j], lst[i+1][j+1])
        lst[i][j] = lst[i][j] + value

print(lst[0][0])