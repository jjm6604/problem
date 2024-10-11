def solution(diffs, times, limit):
    answer = 0
    N = len(diffs)
    n = 0
    times.append(0)
    start, end = 1, 100000
    
    def puzzle(level, limit):

        time_sum = 0
        for i in range(N):
            if diffs[i] > level:
                time = (times[i-1] + times[i]) * (diffs[i] - level) + times[i]
            else:
                time = times[i]
            time_sum += time
            if time_sum > limit:
                return False

        return True
    
    while start <= end:
        mid = (start + end) // 2
        
        if puzzle(mid, limit):
            end = mid - 1
        else:
            start = mid + 1
    
    
    answer = max(start, end)
        
    return answer



    
    