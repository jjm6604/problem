def cal(team):
    score1 = 0
    score2 = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if i in team and j in team:
                score1 += MAP[i][j]
            elif i not in team and j not in team:
                score2 += MAP[i][j]

    scores.add(abs(score1 - score2))
    return


def backtrack(team, n, k):
    if n == (N//2):
        cal(team)
        return
    for i in range(k, N):
        if selected[i] == 0:
            selected[i] = 1
            backtrack(team + [i], n+1, i+1)
            selected[i] = 0
            
            
N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
selected = [0] * N
scores = set()
backtrack([], 0, 0)
print(min(scores))