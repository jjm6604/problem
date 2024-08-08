direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

value = float('inf')


def solution(maze):
    answer = 0
    N, M = len(maze), len(maze[0])
    v = [[[0] * M for _ in range(N)] for _ in range(2)]
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                red = [i, j, True]
                v[0][i][j] = 1
            if maze[i][j] == 2:
                blue = [i, j, True]
                v[1][i][j] = 1
    def backtrack(r, b, cnt):
        global value

        if cnt >= value:
            return
        if not r[2] and not b[2]:
            if value > cnt:
                value = cnt
            return
        else:
            for i in range(4):
                if r[2]:
                    rx, ry = r[0] + direct[i][0], r[1] + direct[i][1]
                else:
                    rx, ry = r[0], r[1]
                for j in range(4):
                    if b[2]:
                        bx, by = b[0] + direct[j][0], b[1] + direct[j][1]
                    else:
                        bx, by = b[0], b[1]
                    if 0 <= rx < N and 0 <= bx < N and 0 <= ry < M and 0 <= by < M and (
                            v[0][rx][ry] == 0 or not r[2]) and (v[1][bx][by] == 0 or not b[2]) and not (
                            rx == bx and ry == by) and not (rx == b[0] and ry == b[1] and bx == r[0] and by == r[1]) and \
                            maze[rx][ry] != 5 and maze[bx][by] != 5:

                        v[0][rx][ry] += 1
                        v[1][bx][by] += 1

                        r_flag = r[2]
                        b_flag = b[2]
                        if maze[rx][ry] == 3:
                            r_flag = False
                        if maze[bx][by] == 4:
                            b_flag = False
                        backtrack([rx, ry, r_flag], [bx, by, b_flag], cnt + 1)
                        v[0][rx][ry] -= 1
                        v[1][bx][by] -= 1


    backtrack(red, blue, 0)
    if value < float('inf'):
        answer = value
    return answer