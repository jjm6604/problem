def solution(cards1, cards2, goal):
    answer = 'Yes'
    while len(goal) > 0:
        if cards1 and goal[0] == cards1[0]:
            goal.pop(0)
            cards1.pop(0)
        elif cards2 and goal[0] == cards2[0]:
            goal.pop(0)
            cards2.pop(0)
        else:
            answer = 'No'
            break
    return answer