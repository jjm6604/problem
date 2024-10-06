def solution(s):
    answer = 1
    N = len(s)
    
    for i in range(1, N):
        n = 1
        odd_cnt = 1
        even_cnt = 0
        
        if answer // 2 > (N - i):
            break
        
        while True:
            front, back = i - n, i + n
            if 0 > front or back >= N:
                break
            if s[front] == s[back]:
                n += 1
                odd_cnt += 2
            else:
                break
                
        n = 0
        while True:
            front, back = i - 1 - n, i + n
            if 0 > front or back >= N:
                break
            if s[front] == s[back]:
                n += 1
                even_cnt += 2
            else:
                break
                
        cnt = max(odd_cnt, even_cnt)   
        if cnt > answer:
            answer = cnt
            
    return answer