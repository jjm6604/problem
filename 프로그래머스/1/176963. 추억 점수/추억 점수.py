def solution(name, yearning, photo):
    answer = []
    score_dict = {}
    for i in range(len(name)):
        score_dict[name[i]] = yearning[i]
    
    for p in photo:
        score = 0
        for person in p:
            score += score_dict.get(person, 0)
        answer.append(score)
    
    return answer