def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        if word == '':
            answer += ' '
            continue
            
        if 'a' <= word[0] <= 'z':
            answer += chr(ord(word[0]) - 32)
        else:
            answer += word[0]
        
        for i in range(1, len(word)):
            if 'A' <= word[i] <= 'Z':
                answer += chr(ord(word[i]) + 32)
            else:
                answer += word[i]
        answer += ' '
        
    answer = answer [:-1]
    
    return answer