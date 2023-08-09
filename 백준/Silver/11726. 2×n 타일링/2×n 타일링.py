A = [0, 1, 2, 3, 5]
N = int(input())
for i in range(5, N+1):
    A.append((A[i-2] + A[i-1])%10007)

print(A[N])