def solution(scores):
    answer = 1
    N = len(scores)
    wanho = scores[0]
    wanho_score = sum(wanho)
    for i in range(1, N):
        if wanho[0] < scores[i][0] and wanho[1] < scores[i][1]:
            answer = -1

    if answer != -1:
        scores.sort(key=lambda x:x[0])
        score_lst = []
        score_dict = {}
        for i in range(N):
            if score_dict.get(scores[i][0], -1) == -1:
                score_lst.append(scores[i][0])
                score_dict[scores[i][0]] = scores[i][1]
            else:
                if score_dict[scores[i][0]] < scores[i][1]:
                    score_dict[scores[i][0]] = scores[i][1]
        idx = 0
        M = len(score_lst)
        max_score = score_lst[M-1]
        max_idx = N
        for i in range(N):
            sum_score = scores[i][0] + scores[i][1]
            while score_lst[idx] != scores[i][0]:
                idx += 1
            if scores[i][0] == max_score:
                max_idx = i
                break
            if sum_score > wanho_score:
                for j in range(idx + 1, M):
                    if scores[i][1] < score_dict[score_lst[j]]:
                        break
                    else:
                        if j == M-1:
                            answer += 1
    
        for i in range(max_idx, N):
            if sum(scores[i]) > wanho_score:
                answer += 1

        
    return answer