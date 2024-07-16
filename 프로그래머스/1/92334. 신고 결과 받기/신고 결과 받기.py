def solution(id_list, report, k):
    N = len(id_list)
    id_dict = {}
    checked = [[0] * N for _ in range(N)]
    cnt = [0] * N
    result = [0] * N
    
    for i in range(N):
        id_dict[id_list[i]] = i
    
    for r in report:
        user1, user2 = r.split()
        if checked[id_dict[user1]][id_dict[user2]] == 0:
            checked[id_dict[user1]][id_dict[user2]] = 1
            cnt[id_dict[user2]] += 1
            
    for i in range(N):
        if cnt[i] >= k:
            for j in range(N):
                if checked[j][i] == 1:
                    result[j] += 1
                    
    return result