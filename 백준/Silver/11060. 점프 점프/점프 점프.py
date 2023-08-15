N = int(input())
lst = list(map(int, input().split()))
A = [1001] * (N+101)
A[0], A[1] = 0, 0
for i in range(1, N+1):
    for j in range(1, lst[i-1]+1):
        if A[i+j] > A[i] + 1:
            A[i+j] = A[i] + 1
if A[N] == 1001:
    A[N] = -1
print(A[N])
