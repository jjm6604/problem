N = int(input())
A = list(map(int, input().split()))

B = [0] * N
B[0] = A[0]
for i in range(1, len(A)):
    if B[i-1] + A[i] < A[i]:
        B[i] = A[i]
    else:
        B[i] = B[i-1] + A[i]

print(max(B))