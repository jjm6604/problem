N = int(input())
n = int(input())
lst = [0]
for i in range(N-1):
    lst.append(int(input()))
cnt = 0
while True:
    if n > max(lst):
        break
    lst.sort()
    lst[N-1] -= 1
    n += 1
    cnt += 1
print(cnt)