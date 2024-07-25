def solution(s):
    answer = 0
    flag = True
    for i in range(len(s)):
        if flag:
            answer += 1
            start = s[i]
            cnt1 = 0
            cnt2 = 0
            flag = False
            
        if s[i] == start:
            cnt2 += 1
        else:
            cnt1 += 1
        if cnt1 == cnt2:
            flag = True
    return answer