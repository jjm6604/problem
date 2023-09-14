import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst1 = [input().strip() for _ in range(N)]
lst2 = set([input().strip() for _ in range(M)])
lst1.sort()
n = 0
result = []
for lst in lst1:
    if lst in lst2:
        result.append(lst)
        lst2.remove(lst)

print(len(result))
for res in result:
    print(res)