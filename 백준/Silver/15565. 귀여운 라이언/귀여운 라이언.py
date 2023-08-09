import sys
N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
min_size = N+1
start = 0
cnt = 0
for end in range(N):
    if lst[end] == 1:
        cnt += 1

    if cnt == K:
        while lst[start] != 1:
            start += 1
        min_size = min(min_size, end-start+1)
        start += 1
        cnt -= 1
if min_size == N+1:
    print(-1)
else:
    print(min_size)