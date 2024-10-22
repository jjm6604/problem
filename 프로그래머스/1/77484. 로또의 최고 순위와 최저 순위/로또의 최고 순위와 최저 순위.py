def solution(lottos, win_nums):
    answer = []
    win_dict = {2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    
    cnt = 0
    zero = 0
    
    for lotto in lottos:
        if lotto in win_nums: 
            cnt += 1
        if lotto == 0:
            zero += 1
    
    answer = [win_dict.get(cnt + zero, 6), win_dict.get(cnt, 6)]
    
    return answer