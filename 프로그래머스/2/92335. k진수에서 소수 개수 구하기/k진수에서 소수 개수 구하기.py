def change(N, K):
    num = ''
    while N:
        num = str(N % K) + num
        N //= K
    return num


def prime_number(k):
    if k == 1:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    numbers = change(n, k).split('0')
    prime = set()
    
    for number in numbers:
        if number:
            if number in prime:
                answer += 1
            elif prime_number(int(number)):
                answer += 1
                prime.add(number)
    
    return answer