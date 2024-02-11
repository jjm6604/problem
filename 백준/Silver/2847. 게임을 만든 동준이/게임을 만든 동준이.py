n = int(input())
lst = []
count = 0
for i in range(n):
    lst.insert(0, int(input()))

for i in range(1, n):
    while lst[i] >= lst[i-1]:
        lst[i] -= 1
        count += 1
print(count)