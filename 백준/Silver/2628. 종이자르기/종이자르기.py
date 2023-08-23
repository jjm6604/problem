
a, b = map(int, input().split())
lst = [[0] * a for _ in range(b)]
n = int(input())
lst1 = [0, b]
lst2 = [0, a]
for i in range(n):
    x, length = map(int, input().split())
    if x == 0:
        lst1.append(length)
    else:
        lst2.append(length)
lst1.sort()
lst2.sort()
result = []
for i in range(1, len(lst1)):
    len_b = lst1[i] - lst1[i-1]
    for j in range(1, len(lst2)):
        len_a = lst2[j] - lst2[j-1]
        result.append(len_a*len_b)
print(max(result))