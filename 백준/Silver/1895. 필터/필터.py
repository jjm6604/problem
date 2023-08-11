R, C = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(R)]
T = int(input())

cnt = 0
for i in range(1, R-1):
    for j in range(1, C-1):
        new_lst = []
        for k in range(-1, 2):
            new_lst += lst[i+k][j-1:j+2]
        new_lst.sort()
        if new_lst[4] >= T:
            cnt += 1
print(cnt)