def get_divisor(n):
    cnt = 0
    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            cnt += 1
            if (i != (n // i)): 
                cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        N = get_divisor(i)
        if N % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer