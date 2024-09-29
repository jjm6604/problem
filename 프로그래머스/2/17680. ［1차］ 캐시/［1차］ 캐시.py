def solution(cacheSize, cities):
    answer = 0
    cache = []
    N = len(cities)
    k = 0
    for i in range(N):
        city = cities[i].upper()
        for j in range(max(0, i-cacheSize-k), i-k):
            if cache[j] == city:
                answer += 1
                cache.pop(j)
                k += 1
                break
        else:
            answer += 5
        cache.append(city)
        
    
    return answer