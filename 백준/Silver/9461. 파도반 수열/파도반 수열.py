N = int(input())

for n in range(N):
    A = [1, 1, 1, 2, 2]
    num = int(input())
    for i in range(5, num):
        A.append(A[i-5] + A[i-1])
    print(A[num-1])