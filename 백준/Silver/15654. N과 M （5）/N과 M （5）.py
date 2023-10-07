def backtrack(k, n):
    if n == M:
        print(*lst)
        return
    for i in range(N):
        if checked[i] == 0:
            lst.append(nums[i])
            checked[i] = 1
            backtrack(i+1, n+1)
            lst.pop()
            checked[i] = 0

            
N, M = map(int, input().split())
nums = list(map(int, input().split()))
checked = [0] * N
nums.sort()
lst = []
backtrack(0, 0)