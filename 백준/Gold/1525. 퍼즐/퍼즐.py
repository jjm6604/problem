from collections import deque

direct = [1, -1, 3, -3]

MAP = [list(input().split()) for _ in range(3)]
board_str = ''
for i in range(3):
    for j in range(3):
        board_str += MAP[i][j]
nums = set()
q = deque()

start = board_str.index('0')

q.append((board_str, start, 0))


while q:
    board, x, cnt = q.popleft()
    if board == '123456780':
        print(cnt)
        exit()

    for i in range(4):
        dx = x + direct[i]
        if 0 <= dx < 9:
            if (2 <= i < 4) or (0 <= i < 2 and (x // 3) == (dx // 3)):

                new_board = list(board)
                new_board[dx], new_board[x] = new_board[x], new_board[dx]
                new_board_str = ''.join(new_board)
                if new_board_str not in nums:
                    nums.add(new_board_str)
                    q.append((new_board_str, dx, cnt + 1))



print(-1)