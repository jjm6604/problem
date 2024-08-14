def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people) - 1
    
    while True:
        if i > j:
            break
        if people[i] + people[j] <= limit:
            answer += 1
            i += 1
            j -= 1
        else:
            answer += 1
            j -= 1
    return answer