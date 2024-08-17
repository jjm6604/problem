def solution(record):
    answer = []
    chat = []
    nickname = {}
    
    for r in record:
        action = r.split()
        if action[0] != 'Change':
            chat.append([action[0], action[1]])
        if action[0] != 'Leave':
            nickname[action[1]] = action[2]
    
    for c in chat:
        if c[0] == 'Enter':
            answer.append(f'{nickname[c[1]]}님이 들어왔습니다.')
        else:
            answer.append(f'{nickname[c[1]]}님이 나갔습니다.')
            
    return answer