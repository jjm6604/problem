

def solution(order):
    answer = 0
    s = []
    N = len(order)
    n = 1
    i = 0
    k = 1
    while i < N:
        if order[i] == k:
            k += 1
            i += 1
            answer += 1
        elif s and order[i] == s[len(s) - 1]:
            i += 1
            answer += 1
            s.pop()

        else:
            if k == N:
                break
            s.append(k)
            k += 1
            
    return answer