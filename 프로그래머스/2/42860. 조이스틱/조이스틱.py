from collections import deque

def solution(name):
    answer = 999999999
    word = {}
    for i in range(26):
        word[chr(65 + i)] = min(i, 26 - i)
    
    N = len(name)
    checked = [[] for _ in range(N)]
    q = deque()
    q.append(['A' * N, 0, 0])
    
    while q:
        x, idx, cnt = q.popleft()
        if x == name:
            if answer > cnt:
                answer = max(0, cnt - 1)
            continue
        if x not in checked[idx]:
            checked[idx].append(x)
            if name[idx] != x[idx]:
                x = x[:idx] + name[idx] + x[idx+1:]
                cnt += word[name[idx]]
                
            q.append([x, (idx+1) % N, cnt + 1])
            q.append([x, ((idx-1) + N) % N, cnt + 1])

        
        
    return answer