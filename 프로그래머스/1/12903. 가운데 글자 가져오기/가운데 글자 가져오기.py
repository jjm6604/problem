def solution(s):
    answer = ''
    N = len(s)
    if N % 2 == 0:
        answer = s[N // 2 - 1: N // 2 + 1]
    else:
        answer = s[N // 2]
    return answer