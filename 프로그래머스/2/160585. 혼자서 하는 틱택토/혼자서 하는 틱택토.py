def solution(board):
    answer = 1
    O = 0
    X = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                O += 1
            elif board[i][j] == 'X':
                X += 1
    if not (O - X == 0 or O - X == 1):
        answer = 0
        
    x_flag = 0
    o_flag = 0
    for i in range(3):
        x_start = board[i][0]
        y_start = board[0][i]
        x_cnt = 1
        y_cnt = 1
        for j in range(1, 3):
            if board[i][j] == x_start:
                x_cnt += 1
            if board[j][i] == y_start:
                y_cnt += 1
        if x_cnt == 3:
            if x_start == 'O':
                o_flag += 1
            elif x_start == 'X':
                x_flag += 1
        if y_cnt == 3:
            if y_start == 'O':
                o_flag += 1
            elif y_start == 'X':
                x_flag += 1
        
    start_0 = board[0][0]
    start_2 = board[0][2]
    cnt_0 = 1
    cnt_2 = 1
    
    for i in range(1, 3):
        if board[i][i] == start_0:
            cnt_0 += 1
        if board[i][2-i] == start_2:
            cnt_2 += 1
            
    if cnt_0 == 3:
        if start_0 == 'O':
            o_flag += 1
        elif start_0 == 'X':
            x_flag += 1
            
    if cnt_2 == 3:
        if start_2 == 'O':
            o_flag += 1
        elif start_2 == 'X':
            x_flag += 1
    
    if x_flag and o_flag:
        answer = 0
    
    if (O - X == 1 and x_flag) or (O - X == 0 and o_flag):
        answer = 0

    return answer