def solution(phone_number):
    answer = ''
    
    N = len(phone_number) - 4
    number = phone_number[N: N + 4]
    answer = '*' * N + number
    
    return answer