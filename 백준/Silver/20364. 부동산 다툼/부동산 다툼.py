def node(n):
    global result
    if tree[n] != 0:
        result = n
    if n == 1:
        print(result)
        return
    node(n//2)
V, Q = map(int,input().split())
tree = [0] * (V+1)
lst = []

for i in range(Q):
    lst.append(int(input()))
for i in range(Q):
    result = 0
    node(lst[i])
    tree[lst[i]] = 1
