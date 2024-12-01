
def solution(weights):
    answer = 0
    
    weight_dict = {}
    weight_cnt = {}
    weights.sort()
    
    for weight in weights:
        weight_cnt[weight] = weight_cnt.get(weight, 0) + 1
        for i in range(2, 5):
            w = weight * i
            weight_dict[w] = weight_dict.get(w, 0) + 1
    
    for weight in weight_cnt.values():
        if weight >= 2:
            answer -= weight * (weight - 1)
            
    for weight in weight_dict.values():
        if weight >= 2:
            answer += weight * (weight - 1) / 2
    
    return answer