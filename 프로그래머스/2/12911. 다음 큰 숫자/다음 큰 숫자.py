def change(number):
    result = ''
    
    while number:
        result = str(number % 2) + result
        number //= 2
    return '0' + result
    
    
def solution(n):
    answer = 0
    num = change(n)
    N = len(num)
    one = 0
    for i in range(N-1, -1, -1):
        if num[i] == '1':
            one += 1
        if one and num[i] == '0':
            zero = i
            break
            
    zero_cnt = N - zero - 1 - one
    next_num = num[:zero] + '10' + '0' * zero_cnt + (one - 1) * '1'
    
    length = len(next_num)
    
    for i in range(length):
        if next_num[i] == '1':
            answer += 2 ** (length - 1 - i)
    
    return answer