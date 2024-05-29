direct = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

def solution(park, routes):
    answer = []
    
    N = len(park)
    M = len(park[0])
    for i in range(N):
        for j in range(M):
            if park[i][j] == 'S':
                point = [i, j]
    
    for route in routes:
        go, value = route.split()
        go_point = point[:]
        for j in range(int(value)):
            go_point = [go_point[0] + direct[go][0], go_point[1] + direct[go][1]] 
            if go_point[0] < 0 or go_point[0] >= N or go_point[1] < 0 or go_point[1] >= M or park[go_point[0]][go_point[1]] == 'X':
                break
        else:
            point = go_point
            
    answer = point
    return answer