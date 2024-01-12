def backtrack(n, m, nums):

    if len(nums) == 6:
        print(*nums)
        return
    if m == lst[0]:
        return
    backtrack(n+1, m+1, nums + [lst[m+1]])
    backtrack(n, m+1, nums)

while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        exit()
    nums = []
    backtrack(0, 0, [])
    print()
