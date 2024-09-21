def solution(number, k):
    answer = ''
    N = len(number)
    cnt = 0
    value = int(number[0])
    result = [10, value]
    
    for i in range(1, N):
        num = int(number[i])
        if num > value:
            while num > value:
                result.pop()
                value = result[-1]
                cnt += 1
                if cnt == k:
                    break
            else:
                value = num
                result.append(num)
        else:
            result.append(num)
            value = num
        if cnt == k:
            result.append(int(number[i:N]))
            break
            
    for i in range(k - cnt):
        result.pop()
        
    answer = "".join(map(str, result[1:]))
    
    return answer