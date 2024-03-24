T = int(input())

for t in range(T):
    N = int(input())
    cnt = 0
    winner = [0, 0]
    flag = True
    for i in range(1, N+1):
        n = int(input())
        cnt += n
        if winner[0] < n:
            winner[0] = n
            winner[1] = i
            flag = True
        elif winner[0] == n:
            flag = False

    if flag:
        if cnt // winner[0] < 2:
            print(f'majority winner {winner[1]}')
        else:
            print(f'minority winner {winner[1]}')

    else:
        print('no winner')