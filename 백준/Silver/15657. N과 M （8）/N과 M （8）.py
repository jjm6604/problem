def backtrack(m, k):
    if m == M:
        print(*lst)
        return
    for i in range(k, N):
        lst.append(nums[i])
        backtrack(m+1, i)
        lst.pop()
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = []
backtrack(0, 0)

