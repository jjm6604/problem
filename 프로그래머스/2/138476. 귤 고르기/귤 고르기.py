nums = set()
res = set()
def solution(k, tangerine):
    answer = 0
    temp_cnt = set()
    size_dict = {}
    for t in tangerine:
        if size_dict.get(t, -1) == -1:
            size_dict[t] = 1
        else:
            size_dict[t] += 1
    cnt_lst = list(size_dict.values())
    cnt_lst.sort(reverse = True)
    cnt_sum = 0
    answer = -1
    for i in range(len(cnt_lst)):
        cnt_sum += cnt_lst[i]
        if cnt_sum >= k:
            answer = i + 1
            break
    
        
    return answer

