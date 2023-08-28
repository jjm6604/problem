a = []
b = []
total = []
N = int(input())
for _ in range(6):
    c, d = map(int, input().split())
    if c == 1 or c == 2:
        a.append(d)
    else:
        b.append(d)
    total.append(d)
max_a = max(a)
max_b = max(b)
a_idx = total.index(max_a)
b_idx = total.index(max_b)
result = max_a * max_b - (abs(total[a_idx-1] - total[a_idx-5]) * abs(total[b_idx-1] - total[b_idx-5]))
print(result * N)