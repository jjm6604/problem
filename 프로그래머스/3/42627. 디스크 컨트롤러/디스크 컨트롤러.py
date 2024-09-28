import heapq

def solution(jobs):
    answer = 0
    N = len(jobs)
    total_time = 0
    jobs.sort(key=lambda x: (x[0], x[1]))
    n = 0
    working = False
    time = 0
    work_lst = []
    end_time = -1
    
    while True:
        if time == end_time:
            if work_lst:
                end_time = time + heapq.heappop(work_lst)
            else:
                working = False
                
        if working:
            total_time += 1
            
        if n < N and time == jobs[n][0]:
            while n < N:
                if jobs[n][0] == time:
                    if working:
                        heapq.heappush(work_lst, jobs[n][1])
                    else:
                        working = True
                        end_time = time + jobs[n][1]
                else:
                    break    
                n += 1
            
        if n == N and len(work_lst) == 0:
            total_time += end_time - time
            break
        
        total_time += len(work_lst)
        time += 1
        
    answer = total_time // N
    return answer