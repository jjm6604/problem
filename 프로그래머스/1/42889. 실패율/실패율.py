def solution(N, stages):
    answer = []
    
    cnt = [0] * (N+2)
    total = []
    for stage in stages:
        cnt[stage] += 1
    
    n = cnt[N+1]
    for i in range(N, 0, -1):
        n += cnt[i]
        if cnt[i] == 0:
            total.append([i, 0])
        else:
            total.append([i, (cnt[i] / n)])
    
    total.sort(key=lambda x: x[0])
    total.sort(key=lambda x: x[1], reverse=True)
    
    for t in total:
        answer.append(t[0])
    return answer