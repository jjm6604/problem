import heapq

def solution(n, k, enemy):
    N = len(enemy)
    heap = []
    answer = 0
    
    for i in range(N):
        n -= enemy[i]
        heapq.heappush(heap, -enemy[i])
        answer += 1
        if n < 0:
            if k:
                n -= heapq.heappop(heap)
                k -= 1
            else:
                answer -= 1
                break
                
            
    return answer