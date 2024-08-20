def solution(n, left, right):
    answer = []
    # 1234 2234 3334 4444
    N = left // n + 1
    M = right // n + 2
    
    start = left % n
    end = right % n
    
    numbers = []
    
    for i in range(n):
        numbers.append(i+1)
        
    for i in range(N, M):
        row = [i] * i + numbers[i:]
        answer += row
        
    length = len(answer)
    answer = answer[start: length - n + end + 1]
    
    
    return answer