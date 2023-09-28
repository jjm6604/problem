def backtrack(cnt):
    if cnt == M:
        print(*lst)
        return
    for i in range(N):
        if checked[i] == 0:
            checked[i] = 1
            lst.append(nums[i])
            backtrack(cnt+1)
            lst.pop()
            checked[i] = 0


N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
checked = [0] * N
lst = []
backtrack(0)