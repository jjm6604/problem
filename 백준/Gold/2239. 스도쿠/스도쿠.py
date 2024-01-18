def check(x, y):
    # 가로
    checked = [0] * 10
    for i in range(9):
        checked[board[x][i]] += 1
    for i in range(1,10):
        if checked[i] > 1:
            return False

    # 세로
    checked = [0] * 10
    for i in range(9):
        checked[board[i][y]] += 1
    for i in range(1,10):
        if checked[i] > 1:
            return False

    # 3X3 박스
    checked = [0] * 10
    for i in range(3):
        for j in range(3):
            checked[board[(x // 3) * 3 + i][(y // 3) * 3 + j]] += 1
    for i in range(1,10):
        if checked[i] > 1:
            return False

    return True


def backtrack(n):
    if n == cnt:
        for i in range(9):
            for j in range(9):
                print(board[i][j], end='')
            print()
        exit(0)


    x, y = lst[n][0], lst[n][1]
    for i in range(1, 10):
        board[x][y] = i
        if check(x, y):
            backtrack(n+1)
        board[x][y] = 0


board = [list(map(int, input())) for _ in range(9)]

lst = []
cnt = 0
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            lst.append((i, j))
            cnt += 1
backtrack(0)