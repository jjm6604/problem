def solution(n,a,b):
    answer = 0
    lst = [i for i in range(1, n+1)]
    k = 0
    while True:
        temp = []
        N = len(lst)
        k += 1
        for i in range(0, N, 2):
            if lst[i] in (a, b) and lst[i+1] in (a, b):
                return k
            elif lst[i] in (a, b):
                temp.append(lst[i])
            elif lst[i+1] in (a, b):
                temp.append(lst[i+1])
            else:
                temp.append(lst[i])
        lst = temp[:]
    return answer