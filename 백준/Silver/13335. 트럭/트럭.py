n, w, L = map(int, input().split())
lst = list(map(int, input().split()))
q = [0] * w
time = 0
while True:
    q.pop(0)
    if sum(q) + lst[0] <= L:
        q.append(lst.pop(0))
    else:
        q.append(0)
    time += 1
    if not lst:
        break
time += w
print(time)