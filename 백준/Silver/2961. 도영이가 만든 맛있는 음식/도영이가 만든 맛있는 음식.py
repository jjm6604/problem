import sys
input = sys.stdin.readline

def cal(n):
    if n == N:
        select_lst.append(select[:])
        return
    select[n] = 1
    cal(n+1)
    select[n] = 0
    cal(n+1)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
select = [0] * N
select_lst = []
result = abs(lst[0][0]-lst[0][1])
cal(0)
select_lst.pop()
for s in select_lst:
    sum1 = 1
    sum2 = 0
    for i in range(N):
        if s[i] == 1:
            sum1 *= lst[i][0]
            sum2 += lst[i][1]
    if result > abs(sum1-sum2):
        result = abs(sum1-sum2)
print(result)
