n = int(input())

money_list = []
sum = 0

for i in range(n):
    money_list.append(int(input()))

money_list.sort()
money_list.reverse()

for i in range(n):
    if (i+1) % 3 != 0:
        sum += money_list[i]

print(sum)