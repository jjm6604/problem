A = [0, 0, 1, 1, 2, 3, 3]
# 1 2 3 4 5 6

num = int(input())

for i in range(7, num+1):
    a1 = a2 = i - 1
    if i % 3 == 0:
        a1 = i // 3
    if i % 2 == 0:
        a2 = i // 2
    a3 = i - 1
    number = min(A[a1], A[a2], A[a3]) + 1
    A.append(number)

print(A[num])
