def solution(s):
    answer = []
    word = {}
    for i in range(97, 123):
        word[chr(i)] = -1
    for i in range(len(s)):
        if word[s[i]] == -1:
            idx = -1
        else:
            idx = i - word[s[i]]
        answer.append(idx)
        word[s[i]] = i
    return answer