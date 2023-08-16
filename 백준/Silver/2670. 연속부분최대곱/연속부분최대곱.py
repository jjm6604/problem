N = int(input())
lst = []
for n in range(N):
    lst.append(float(input()))
A = [lst[0]]
for i in range(1, N):
    if A[i-1] * lst[i] > lst[i]:
        A.append(A[i-1] * lst[i])
    else:
        A.append(lst[i])
print('%.3f'% max(A))