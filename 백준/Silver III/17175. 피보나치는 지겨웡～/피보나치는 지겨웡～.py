N = int(input())

A = [1, 1, 3, 5]

for i in range(4, N+1):
    A.append((A[i-1] + A[i-2] + 1) % 1000000007)
print(A[N])
