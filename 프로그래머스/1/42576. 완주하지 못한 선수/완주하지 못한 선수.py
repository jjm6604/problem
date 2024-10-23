def solution(participant, completion):
    answer = ''
    completion_dict = {}
    
    for i in completion:
        completion_dict[i] = completion_dict.get(i, 0) + 1    
        
    for i in participant:
        if completion_dict.get(i, 0) == 0:
            return i
        completion_dict[i] -= 1
        
    return answer
