def backtrack(x, y, k):
    global res
    if k == K:
        if x == end[0] and y == end[1]:
            res += 1
        return
    if x == end[0] and y == end[1]:
        return
    for i in range(4):
        dx, dy = x + direct[i][0], y + direct[i][1]
        if 0 <= dx < R and 0 <= dy < C and v[dx][dy] == 0 and MAP[dx][dy] == '.':
            v[dx][dy] = 1
            backtrack(dx, dy, k+1)
            v[dx][dy] = 0

R, C, K = map(int, input().split())
MAP = [input() for _ in range(R)]
start = (R-1, 0)
end = (0, C-1)
direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
v = [[0] * C for _ in range(R)]
res = 0
v[start[0]][start[1]] = 1
backtrack(start[0], start[1], 1)
print(res)