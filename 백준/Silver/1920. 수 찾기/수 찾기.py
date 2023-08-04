def cal(A, N, M):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == M:
            return 1
        elif A[mid] > M:
            end = mid - 1
        else:
            start = mid + 1
    return 0

T = int(input())
lst = list(map(int, input().split()))
num = int(input())
target_lst = list(map(int, input().split()))
lst.sort()

for target in target_lst:
    print(cal(lst, T, target))