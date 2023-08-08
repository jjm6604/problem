N = input()

lst = [0] * 10

for n in N:
    lst[int(n)] += 1

if (lst[6] + lst[9]) % 2 == 0:
    lst[6] = (lst[6] + lst[9])//2
else:
    lst[6] = (lst[6] + lst[9]) // 2 + 1

MAX = lst[0]

for i in range(1,9):
    if MAX < lst[i]:
        MAX = lst[i]
print(MAX)