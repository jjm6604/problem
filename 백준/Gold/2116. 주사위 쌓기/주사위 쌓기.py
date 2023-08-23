N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
score = [5, 3, 4, 1, 2, 0]
result = []
floor = 0
for i in range(6):
    sum_score = 0
    a = lst[0][i] # i 홀수일때
    b = lst[0][score[i]] # i 짝수일때
    floor = b
    for j in range(0, N):
        MAX = 0
        floor_idx = lst[j].index(floor)
        for k in range(6):
            if lst[j][k] != floor and score[floor_idx] != k:
                if MAX < lst[j][k]:
                    MAX = lst[j][k]
        sum_score += MAX
        floor = lst[j][score[floor_idx]]
    result.append(sum_score)
print(max(result))