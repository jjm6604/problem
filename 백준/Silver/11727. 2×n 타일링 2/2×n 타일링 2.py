N = int(input())
A = [0, 1, 3]
for i in range(3, N+1):
    A.append((A[i-2] * 2 + A[i-1])%10007)
print(A[N])