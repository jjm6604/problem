def solution(n, m, section):
    answer = 0
    k = 0
    i = 0
    length = len(section)
    while True:
        if i == length:
            break
        if section[i] == k:
            k += (m - 1)
            answer += 1
            while True:
                if section[i] > k:
                    break
                else:
                    i += 1
                    if i == length:
                        break
        else:
            k += 1
    return answer