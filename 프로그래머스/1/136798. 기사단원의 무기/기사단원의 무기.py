def get_divisor(n, limit, power):
    n = int(n)
    divisors = []
    divisors_back = [] 
    cnt = 0
    
    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            cnt += 1
            if (i != (n // i)): 
                cnt += 1
        if cnt > limit:
            return power
    return cnt

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        answer += get_divisor(i, limit, power)
    return answer