N = int(input())
s = []
score = 0
for i in range(N):
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        if s:
            lst = s.pop()
        else:
            continue
    lst[2] -= 1
    if lst[2] == 0:
        score += lst[1]
    else:
        s.append(lst)
print(score)