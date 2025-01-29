def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    k = 0
    while True:
        cnt = 0
        flag = True
        for i in range(k, N):
            progresses[i] += speeds[i]
            if flag and progresses[i] >= 100:
                cnt += 1
                k += 1
            else:
                flag = False
        if cnt:
            answer.append(cnt)
        if k == N:
            break
    return answer