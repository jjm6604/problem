def solution(s):
    answer = ''
    
    cnt = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            cnt = 0
        else:
            if cnt % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
            cnt += 1
            
    return answer