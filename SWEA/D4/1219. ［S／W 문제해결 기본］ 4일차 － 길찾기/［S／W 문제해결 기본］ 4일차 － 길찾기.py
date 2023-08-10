def dfs(arr):
    n = 0 # 출발
    stack = []
    visited = [0] * 100
    visited[n] = 1
    while True:
        for w in range(2):
            if arr[w][n] != 0 and visited[arr[w][n]] == 0:
                if arr[w][n] == 99:
                    return 1
                stack.append(n)
                n = arr[w][n]
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return 0

for _ in range(10):
    t, E = map(int, input().split())
    lst = list(map(int, input().split()))
    G = [[0] * 100 for _ in range(2)]
    for i in range(E):
        if G[0][lst[i*2]] == 0:
            G[0][lst[i*2]] = lst[i*2+1]
        else:
            G[1][lst[i*2]] = lst[i*2+1]

    print(f'#{t}', dfs(G))