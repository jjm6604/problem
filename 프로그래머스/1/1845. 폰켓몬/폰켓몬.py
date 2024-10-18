def solution(nums):
    answer = 0
    N = len(nums)
    max_value = len(set(nums))
    
    answer = min(max_value, N // 2)
    return answer