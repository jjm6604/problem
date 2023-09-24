N, K = map(int, input().split())
res = 0
while True:
    num = bin(N)
    n = num.count('1')
    if n <= K:
        break
    N += 1
    res += 1
print(res)