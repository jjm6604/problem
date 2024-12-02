def solution(cards):
    answer = 0
    N = len(cards)
    
    for i in range(N):
        checked = [0] * N
        num = i
        value1 = 0
        while True:
            if checked[num] == 0:
                checked[num] = 1
                value1 += 1
                num = cards[num] - 1
            else:
                break
        for j in range(N):
            second_checked = checked[:]
            value2 = 0
            num = j
            while True:
                if second_checked[num] == 0:
                    second_checked[num] = 1
                    value2 += 1
                    num = cards[num] - 1
                else:
                    break
            if value1 * value2 > answer:
                answer = value1 * value2

    return answer