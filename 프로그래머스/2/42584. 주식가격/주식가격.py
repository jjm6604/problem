def solution(prices):
    price = prices[0]
    s = [(price, 0)]
    N = len(prices)
    answer = [0] * N

    for i in range(1, N):
        if prices[i] < price:
            while s:
                p = s[-1][0]
                if p > prices[i]:
                    time = s.pop()[1]
                    answer[time] = i-time
                else:
                    break
            price = prices[i]
            s.append((price, i))
        else:
            price = prices[i]
            s.append((price, i))
    
    for _, time in s:
        answer[time] = N - time  - 1
        
    return answer