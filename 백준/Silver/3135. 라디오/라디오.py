num_lst = list(map(int, input().split()))
n = int(input())
num_lst2 = []
count = 0
min_count = abs(num_lst[1] - num_lst[0])
for i in range(n):
    num_lst2.append(int(input()))


# num_lst[1]

for i in range(len(num_lst2)):
    count = abs(num_lst2[i] - num_lst[1]) + 1
    if count < min_count:
        min_count = count

print(min_count)