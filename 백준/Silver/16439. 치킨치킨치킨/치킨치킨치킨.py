N, M = map(int, input().split())
likes = [list(map(int, input().split())) for _ in range(N)]
res = 0
for i in range(M-2):
    for j in range(i, M-1):
        for k in range(j, M):
            score = 0
            for like in likes:
                score += max(like[i], like[j], like[k])
            if res < score:
                res = score
print(res)