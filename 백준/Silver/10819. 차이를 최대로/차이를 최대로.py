def cal(numbers):
    s = 0
    for i in range(N-1):
        s += abs(numbers[i] - numbers[i+1])
    return s


def backtrack(n, new_lst):
    global res
    if n == N:
        if res < cal(new_lst):
            res = cal(new_lst)
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            backtrack(n+1, new_lst + [lst[i]])
            v[i] = 0

            
N = int(input())
lst = list(map(int, input().split()))
v = [0] * N

res = 0

backtrack(0, [])

print(res)