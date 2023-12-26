N, A, B = map(int, input().split())


lst = [0] * N
lst[A-1] = -1
lst[B-1] = -1

n = 0

while True:
    n += 1
    new_lst = []
    for i in range(N//2):
        a = lst[2*i]
        b = lst[2*i+1]
        if a == -1 and b == -1:
            print(n)
            exit(0)
        elif a == -1 or b == -1:
            new_lst.append(-1)
        else:
            new_lst.append(0)
    if N % 2 == 1:
        new_lst.append(lst[-1])
    lst = new_lst
    N = len(lst)



