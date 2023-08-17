N = int(input())
lst = []
for i in range(N):
    lst.append(input())
k = 1
length = len(lst[0])
result = length
while k < length:
    num_lst = []
    for i in range(N):
        num = lst[i][length-k:length]
        if num in num_lst:
            break
        num_lst.append(num)
    else:
        result = k
        break
    k += 1
print(result)