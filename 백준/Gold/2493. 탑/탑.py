N = int(input())
lst = list(map(int, input().split()))
stack = []
stack.append([0, lst[0]])
result = [0]
for i in range(1, N):

    while stack:
        idx, length = stack.pop()
        if length >= lst[i]:
            result.append(idx+1)
            stack.append([idx, length])
            break
    else:
        result.append(0)
    stack.append([i, lst[i]])
print(*result)
