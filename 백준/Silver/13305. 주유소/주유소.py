N = int(input())
lst = list(map(int, input().split())) # 거리
oil = list(map(int, input().split())) # 가격
result = 0
min_money = oil[0]
for i in range(N-1):
    if min_money > oil[i]:
        min_money = oil[i]
    result += min_money * lst[i]
print(result)