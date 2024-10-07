def solution(book_time):
    answer = 0
    N = len(book_time)
    room = 0
    time = {}
    book_time.sort()
    now = 0
    n = 0
    
    while n < N:
        if time.get(now, 0) > 0:
            room -= time[now]
            time[now] = 0
        
        while n < N:
            h, m = map(int, book_time[n][0].split(':'))
            in_time = h * 60 + m
            if in_time == now:
                h, m = map(int, book_time[n][1].split(':'))
                out_time = h * 60 + m + 10
                time[out_time] = time.get(out_time, 0) + 1
                n += 1
                room += 1
            else:
                break
                
        if room > answer:
            answer = room
            
        now += 1
        
    return answer