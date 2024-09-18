def solution(n, words):
    answer = [0, 0]
    check = set()
    last = words[0][-1]
    check.add(words[0])
    for i in range(1, len(words)):
        if words[i] not in check and last == words[i][0]:
            check.add(words[i])
            last = words[i][-1]
        else:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break

    return answer