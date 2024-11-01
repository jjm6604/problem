def check(value):
    for i in range(2, value):
        if value % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    N = len(nums)
    
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                num_sum = nums[i] + nums[j] + nums[k]
                if check(num_sum):
                    answer += 1
    
    return answer