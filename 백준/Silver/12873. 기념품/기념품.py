N = int(input())
lst = []
for n in range(N):
    lst.append(n + 1)

i = 1
index = 0
while len(lst) > 1:
    index += (i ** 3) - 1
    if index > len(lst)-1:
        index %= len(lst)
    lst.pop(index)
    i += 1
print(lst[0])