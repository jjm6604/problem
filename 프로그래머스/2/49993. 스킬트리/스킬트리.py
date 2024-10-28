def solution(skill, skill_trees):
    answer = 0
    N = len(skill)
    
    for tree in skill_trees:
        n = 0
        for t in tree:
            if t in skill:
                if skill.index(t) == n:
                    n += 1
                else:
                    break
        else:
            answer += 1
            
    return answer