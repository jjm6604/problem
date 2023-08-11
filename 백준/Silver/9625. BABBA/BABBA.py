N = int(input())
A = [1, 0, 1, 1, 2]
B = [0, 1, 1, 2, 3]

for i in range(5, N+1):
    A.append(B[i-1])
    B.append(A[i-1]+B[i-1])
print(A[N], B[N])