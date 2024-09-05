def solution(key, lock):
    answer = True
    N, M = len(lock), len(key)
    value = 0
    
    

    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                value += 1
    for _ in range(4):
        
        key_coord = []
        for i in range(M):
            for j in range(M):
                if key[i][j] == 1:
                    key_coord.append([i, j])
                    
        for i in range(-M+1, N):
            for j in range(-M+1, N):
                cnt = 0
                for x, y in key_coord:
                    if 0 <= i + x < N and 0 <= j + y < N:
                        if lock[i + x][j + y] == 0:
                            cnt += 1
                        else:
                            break
                else:
                    if value == cnt:
                        return True
        key = [list(reversed(col)) for col in zip(*key)]

                    
    
    return False