N = int(input())
lst = [-1] * N
result = 0

def n_queen(n):
    global result
    if n == N:
        result += 1
        return
    for i in range(N):
        lst[n] = i
        if promising(n):
            n_queen(n+1)

def promising(n):
    for j in range(n):
        if lst[n] == lst[j] or abs(lst[n] - lst[j]) == abs(n - j):
            return False
    return True
n_queen(0)
print(result)
