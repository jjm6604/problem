n = int(input())
A = [0, 1, 1, 1]
for i in range(4, n+1):
    A.append(A[i-1] + A[i-3])
print(A[n])