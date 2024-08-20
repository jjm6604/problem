def solution(dirs):
    answer = 0
    direct_dict = {'R': [0, 1], 'L': [0, -1], 'U': [1, 0], 'D': [-1, 0]}
    visited = set()
    coord = [5, 5]
    
    for d in dirs:
        dx, dy = coord[0] + direct_dict[d][0], coord[1] + direct_dict[d][1]
        if 0 <= dx <= 10 and 0 <= dy <= 10:
            visited.add((coord[0], coord[1], dx, dy))
            visited.add((dx, dy, coord[0], coord[1]))
            coord = [dx, dy]
            
    answer = len(visited) // 2
    
    return answer