n = int(input())

number_list = []
for i in range(n):
    number_list.append(int(input()))

number_list.sort()
number_list.reverse()

sum = 0

for i in range(n):
    tip = number_list[i] - i
    if(tip <= 0):
        break
    sum += tip
print(sum)