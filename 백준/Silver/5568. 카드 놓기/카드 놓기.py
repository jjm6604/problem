def backtrack(n, num):
    if n == K:
        nums.add(num)
        return
    for i in range(N):
        if selected[i] == 0:
            selected[i] = 1
            backtrack(n+1, num + str(cards[i]))
            selected[i] = 0

N = int(input())
K = int(input())
cards = []
selected = [0] * N
for _ in range(N):
    cards.append(int(input()))
nums = set()
backtrack(0, '')
res = len(nums)
print(res)