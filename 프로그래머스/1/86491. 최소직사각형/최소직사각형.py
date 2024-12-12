
def solution(sizes):
    answer = 0
    x, y = 0, 0
    for size in sizes:
        for i in range(2):
            if size[i] > x:
                x = size[i]
    
    for size in sizes:
        value = min(size)
        if value > y:
            y = value
    
    answer = x * y
        
    return answer