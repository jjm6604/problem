t = [1, 1]
N = int(input())
for i in range(2, N+1):
    num = 0
    for j in range(i):
        num += t[i-1-j] * t[j]
    t.append(num)
print(t[N])