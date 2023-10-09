def backtrack(n):
    if n == M:
        print(*lst)
        return
    for i in range(N):
        lst.append(nums[i])
        backtrack(n+1)
        lst.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = []
backtrack(0)