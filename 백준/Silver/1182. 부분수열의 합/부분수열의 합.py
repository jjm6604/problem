N, S = map(int, input().split())
lst = list(map(int, input().split()))
nums = []
res = 0

for i in range(1 << N):
    temp = []
    for j in range(N):
        if i & (1 << j):
            temp.append(lst[j])
    nums.append(temp)

for i in range(1, len(nums)):
    if sum(nums[i]) == S:
        res += 1
print(res)