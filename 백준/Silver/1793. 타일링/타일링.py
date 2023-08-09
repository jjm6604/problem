try:
    while True:
        A = [1, 1, 3]
        N = int(input())
        for i in range(3, N+1):
            A.append(A[i-1] + A [i-2] * 2)
        print(A[N])
except EOFError:
    exit()