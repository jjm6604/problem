def solution(picks, minerals):
    answer = 0
    res = set()
    res.add(float('inf'))
    n = len(minerals)
    fatigue_dict = {"0diamond": 1, "0iron": 1, "0stone": 1,
                   "1diamond": 5, "1iron": 1, "1stone": 1,
                   "2diamond": 25, "2iron": 5, "2stone": 1,}
    def backtrack(lst, fatigue, k):
        if fatigue >= min(res):
            return
        if k == sum(picks):
            
            res.add(fatigue)
            return
        for i in range(3):
            if lst[i] > 0:
                new_lst = lst[:]
                new_lst[i] -= 1
                new_fatigue = fatigue
                for j in range(5 * k, 5 * k + 5):
                    new_fatigue += fatigue_dict[f'{i}{minerals[j]}']
                    if j == n - 1:
                        res.add(new_fatigue)
                        return
                backtrack(new_lst, new_fatigue, k+1)
            
    backtrack(picks, 0, 0)
    print(res)
    answer = min(res)
    return answer