from collections import deque

def solution(s):
    answer = []
    
    def change(number):
        N = len(number)
        n = 0
        cnt = 0
        s = []
        
        while n < N:            
            if number[n] == '0':
                if len(s) >= 2 and s[-1] == '1' and s[-2] == '1':
                    s.pop()
                    s.pop()
                    cnt += 1
                    n += 1
                    continue
            s.append(number[n])
            n += 1
                
        value = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                value = i + 1
                break
                
        s.insert(value, '110' * cnt)
        result = ''.join(s)
        answer.append(result)
        
        return
                
        
    for i in s:
        change(list(i))
    
    return answer