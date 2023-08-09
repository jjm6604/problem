import sys
N = int(sys.stdin.readline())

A = [0] * 3
B = [0] * 3
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    add_max_lst = [0] * 3
    add_min_lst = [0] * 3

    add_max_lst[0] = max(A[0], A[1]) + lst[0]
    add_max_lst[1] = max(A) + lst[1]
    add_max_lst[2] = max(A[1], A[2]) + lst[2]

    add_min_lst[0] = min(B[0], B[1]) + lst[0]
    add_min_lst[1] = min(B) + lst[1]
    add_min_lst[2] = min(B[1], B[2]) + lst[2]

    A = add_max_lst
    B = add_min_lst

print(max(A), min(B))