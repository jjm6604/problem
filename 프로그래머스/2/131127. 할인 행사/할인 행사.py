def solution(want, number, discount):
    answer = 0
    want_dict = {}
    value = sum(number)
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    for i in range(10):
        product = discount[i]
        cnt = want_dict.get(product, -999999)
        if cnt != -999999:
            if cnt > 0:
                value -= 1
            want_dict[product] -= 1
            
    if value == 0:
        answer += 1
        
    for i in range(10, len(discount)):
        old = discount[i-10]
        new = discount[i]
        if new == old:
            if value == 0:
                answer += 1
            continue
        old_cnt = want_dict.get(old, -999999)
        new_cnt = want_dict.get(new, -999999)
        if old_cnt != -999999:
            if old_cnt >= 0:
                value += 1
            want_dict[old] += 1
        if new_cnt != -999999:
            if new_cnt > 0:
                value -= 1
            want_dict[new] -= 1
            
        if value == 0:
            answer += 1
    return answer