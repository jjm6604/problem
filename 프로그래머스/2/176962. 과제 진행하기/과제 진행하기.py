def clock(now):
    hour, minute = now.split(':')
    if minute == '59':
        set_now = str(int(hour) + 1) + ':00'
        if hour[0] == '0' and hour[1] != '9':
            set_now = '0' + set_now
    else:
        zero = ':'
        if minute[0] == '0' and minute[1] != '9':
            zero = ':0'
        set_now = hour + zero + str(int(minute) + 1)

    return set_now


def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])
    name = plans[0][0]
    time = plans[0][1]
    play = int(plans[0][2])
    lst = []
    i = 1
    N = len(plans)

    while True:
        if play == 0:
            answer.append(name)
            if lst:
                name, play = lst.pop()
        if i < N and plans[i][1] == time:
            lst.append([name, play])
            name, play = plans[i][0], int(plans[i][2])
            i += 1
        if len(answer) == N:
            break
        play -= 1
        time = clock(time)
    return answer
