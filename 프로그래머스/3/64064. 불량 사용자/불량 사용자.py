def solution(user_id, banned_id):
    answer = 1
    N, M = len(user_id), len(banned_id)
    checked = [0] * N
    result = set()
    
    def backtrack(n):
        if n == M:
            result.add(''.join(map(str, checked)))
            return
        for i in range(N):
            if checked[i] == 0:
                if len(banned_id[n]) == len(user_id[i]):
                    for j in range(len(banned_id[n])):
                        if banned_id[n][j] not in ['*', user_id[i][j]]:
                            break
                    else:
                        checked[i] = 1
                        backtrack(n+1)
                        checked[i] = 0
    
    backtrack(0)
    
    answer = len(result)
    
    return answer