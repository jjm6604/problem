N = int(input())
nums = list(map(int, input().split()))
K = int(input())

answer = 0

num_dict = {}

for num in nums:
    num_dict[num] = num_dict.get(num, 0) + 1

num_lst = sorted(list(num_dict.keys()))

for num in num_lst:
    n = K - num
    if n < num:
        break
    if n == num:
        answer += num_dict[n] - 1
    elif num_dict.get(n, False):
        answer += num_dict[n]

print(answer)