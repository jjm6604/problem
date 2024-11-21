def solution(s):
    lst = [s[0]]
    N = len(s)
    n = 1
    
    while n < N:
        if not lst:
            lst.append(s[n])
            n += 1
        else:
            if lst[-1] == s[n]:
                while True:
                    if n == N or not lst or lst[-1] != s[n]:
                        break
                    lst.pop()
                    n += 1
                    
            else:
                lst.append(s[n])
                n += 1
            
    if lst:
        return 0
    else:
        return 1
