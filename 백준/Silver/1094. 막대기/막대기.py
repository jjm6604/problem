n = int(input())
k = 64
cnt = 0

while n > 0:
    if n >= k:
        cnt += 1
        n -= k
    else:
        k //= 2
print(cnt)