def solution(numbers):
    answer = 0
    N = len(numbers)
    checked = [0] * N
    nums = set()
    
    def number_make(k, num):
        if num:
            nums.add(int(num))
        if k == N:
            return
        for i in range(N):
            if checked[i] == 0:
                checked[i] = 1
                number_make(k + 1, num + numbers[i])
                checked[i] = 0
    
    def check(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    number_make(0, '')
    
    for num in nums:
        if num >= 2 and check(num):
            answer += 1
    
    return answer



    