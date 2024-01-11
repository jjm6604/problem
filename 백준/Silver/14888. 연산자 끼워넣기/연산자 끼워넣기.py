def backtrack(n, num):
    if n == N:
        res.add(num)
        return
    for j in range(4):
        if lst[j] > 0:
            lst[j] -= 1
            if j == 0:
                backtrack(n+1, num+nums[n])
            elif j == 1:
                backtrack(n+1, num-nums[n])
            elif j == 2:
                backtrack(n+1, num*nums[n])
            else:
                if num < 0 and nums[n] > 0 and ((-num) % nums[n]) > 0:
                    backtrack(n + 1, num // nums[n] + 1)
                else:
                    backtrack(n+1, num // nums[n])

            lst[j] += 1

N = int(input())
nums = list(map(int, input().split()))
lst = list(map(int, input().split()))
# + - * /

res = set()
backtrack(1, nums[0])
print(max(res))
print(min(res))
