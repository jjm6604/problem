
    
def solution(w,h):
    answer = 0

    if w < h:
        S, L = w, h
    else:
        S, L = h, w
    
    N = L / S
    s = 1
    while True:
        if (L * s / S) % 1 == 0:
            l = int(L * s / S)
            break
        else:
            s += 1
    
    answer = w * h
    cnt = L // l
    for i in range(s):
        start = (L * i / S)
        end = start + (L / S)
        start //= 1
        if end % 1 != 0:
            end = int(end + 1)
        answer -= cnt * (end-start)
        
    
    return answer