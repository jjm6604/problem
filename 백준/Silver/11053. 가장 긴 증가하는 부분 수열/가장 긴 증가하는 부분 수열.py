N = int(input())
lst = list(map(int, input().split()))
A = [1]
for i in range(1, N):
    MAX = 0
    for j in range(i):
        if lst[j] < lst[i]:
            if MAX < A[j]:
                MAX = A[j]
    A.append(MAX+1)
print(max(A))