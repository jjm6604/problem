def solution(m, n, startX, startY, balls):
    answer = []
    
    for x, y in balls:
        value = []
        if y != startY:
            for dx, dy in [[-x, y], [2 * m - x, y]]:
                value.append((startX - dx) ** 2 + (startY - dy) ** 2)
        elif x > startX:
            value.append((startX + x) ** 2 + (startY - y) ** 2)
        else:
            value.append((startX - 2 * m + x) ** 2 + (startY - y) ** 2)
        if x != startX:   
            for dx, dy in [[x, -y], [x, 2 * n - y]]:
                value.append((startX - dx) ** 2 + (startY - dy) ** 2)
        elif y > startY:
            value.append((startX - x) ** 2 + (startY + y) ** 2)
        else:
            value.append((startX - x) ** 2 + (startY - 2 * n + y) ** 2)
        
        answer.append(min(value))
        
        
    return answer