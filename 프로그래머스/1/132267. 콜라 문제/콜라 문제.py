def solution(a, b, n):
    answer = 0
    while True:
        if n < a:
            break
        
        answer += b * (n // a)
        n = (n % a) + b * (n // a)
    return answer