def cal(lst):
    chicken_length = 0
    for h in home:
        value = float('inf')
        for l in lst:
            length = abs(h[0] - l[0]) + abs(h[1] - l[1])
            if value > length:
                value = length
        chicken_length += value
    res.add(chicken_length)
def backtrack(n, m, selected):
    if n == M:
        chicken_lst = []
        for s in selected:
            chicken_lst.append(chicken[s])
        selected_chicken.append(chicken_lst)
        return
    for i in range(m, store):
        backtrack(n+1, i+1, selected + [i])


N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
# 0 빈집 // 1 집 // 2 치킨집
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            home.append((i, j))
        if MAP[i][j] == 2:
            chicken.append((i, j))

store = len(chicken)
# selected = [0] * store

selected_chicken = []
backtrack(0, 0, [])
res = set()
for s in selected_chicken:
    cal(s)
print(min(res))