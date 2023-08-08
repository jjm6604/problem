N, S, R = map(int, input().split())
lst1 = list(map(int, input().split())) # 부서진팀
lst2 = list(map(int, input().split())) # 안부서진팀
lst = [1] * (N + 1)
for i in lst1:
    lst[i] -= 1
for i in lst2:
    lst[i] += 1

for i in range(1, N+1):
    if lst[i] == 0:
        if i > 1 and lst[i-1] == 2:
            lst[i] += 1
            lst[i-1] -= 1
        elif i < N and lst[i+1] == 2:
            lst[i] += 1
            lst[i+1] -= 1
print(lst.count(0))