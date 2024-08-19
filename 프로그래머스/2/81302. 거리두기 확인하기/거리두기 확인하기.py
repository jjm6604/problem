from collections import deque

direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solution(places):
    answer = []
    for place in places:
        result = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    q = deque()
                    checked = [[0] * 5 for _ in range(5)]
                    checked[i][j] = 1
                    q.append([i, j, 0])
                    while q and result:
                        x, y, length = q.popleft()
                        if length < 2:
                            for d in direct:
                                dx, dy = x + d[0], y + d[1]
                                if 0 <= dx < 5 and 0 <= dy < 5 and checked[dx][dy] == 0 and place[dx][dy] != 'X':
                                    if place[dx][dy] == 'P':
                                        result = 0
                                    checked[dx][dy] = 1
                                    q.append([dx, dy, length + 1])
        answer.append(result)
        
    return answer

