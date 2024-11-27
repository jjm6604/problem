def solution(arr):
    answer = 0
    n = min(arr)
    k = 1
    N = len(arr)
    
    while True:
        num = n * k
        for i in range(N):
            if num % arr[i] != 0:
                break
        else:
            answer = num
            break
        k += 1
        
    return answer