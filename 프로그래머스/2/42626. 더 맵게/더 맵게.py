import heapq

def solution(scoville, K):
    answer = 0
    scores = []
    
    for s in scoville:
        heapq.heappush(scores, s)
    
    while True:
        first = heapq.heappop(scores)
        if first >= K:
            break
        elif not scores:
            return -1
        else:
            second = heapq.heappop(scores)
            heapq.heappush(scores, first + second * 2)
            answer += 1
    
    return answer