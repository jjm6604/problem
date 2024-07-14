def solution(topping):
    answer = 0
    count1 = set()
    count2 = {}
    for t in topping:
        count2[t] = count2.get(t, 0) + 1
    for t in topping:
        count1.add(t)
        count2[t] -= 1
        if count2[t] == 0:
            count2.pop(t)
        if len(count1) - len(count2) == 0:
            answer += 1
    return answer