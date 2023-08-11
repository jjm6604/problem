H, W = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(H+1):
    s = []
    for j in range(W):
        if lst[j] >= i:
            s.append(j)
        if len(s) == 2:
            cnt += s[1] - s[0] - 1
            s.pop(0)

print(cnt)