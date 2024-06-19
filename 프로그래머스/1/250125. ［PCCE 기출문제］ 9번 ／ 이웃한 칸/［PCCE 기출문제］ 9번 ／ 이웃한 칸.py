def solution(board, h, w):
    answer = 0
    direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    color = board[h][w]
    for d in direct:
        dh, dw = h + d[0], w + d[1]
        if 0 <= dh < len(board) and 0 <= dw < len(board[0]) and board[dh][dw] == color:
            answer += 1
    return answer