def solution(keymap, targets):
    answer = []
    key_dict = {}
    for i in range(65, 91):
        key_dict[chr(i)] = 999
    
    for k in keymap:
        for i in range(len(k)):
            key_dict[k[i]] = min(key_dict[k[i]], i + 1)
    for target in targets:
        value = 0
        for t in target:
            if key_dict[t] == 999:
                value = -1
                break
            else:
                value += key_dict[t]
        answer.append(value)
        
    return answer