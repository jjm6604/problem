def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1
        
    for i in range(begin, end + 1):
        k = 0
        for j in range(2, int(i ** 0.5) + 2):
            if i % j == 0:
                if i // j <= 10000000:
                    answer.append(i // j)
                    break
                k = j
        else:
            if k:
                answer.append(k)
            else:
                answer.append(1)
    return answer