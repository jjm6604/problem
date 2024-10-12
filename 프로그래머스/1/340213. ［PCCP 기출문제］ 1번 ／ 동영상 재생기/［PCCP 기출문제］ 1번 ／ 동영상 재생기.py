def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    time = int(pos[:2]) * 60 + int(pos[3:])
    max_time = int(video_len[:2]) * 60 + int(video_len[3:])
    start = int(op_start[:2]) * 60 + int(op_start[3:])
    end = int(op_end[:2]) * 60 + int(op_end[3:])
        
    if start <= time <= end:
        time = end
        
    for command in commands:
        if command == 'prev':
            time = max(time - 10, 0)
        elif command == 'next':
            time = min(time + 10, max_time)
    
        if start <= time <= end:
            time = end
    
    minutes = time // 60
    seconds = time % 60
    
    if minutes < 10:
        answer += '0' + str(minutes) + ':'
    else:
        answer += str(minutes) + ':'
        
    if seconds < 10:
        answer += '0' + str(seconds)
    else:
        answer += str(seconds)
    
    return answer