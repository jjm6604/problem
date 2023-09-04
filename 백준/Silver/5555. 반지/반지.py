word = input()
N = int(input())
rings = [input() for _ in range(N)]
result = 0
for i in range(N):
    rings[i] = rings[i] + rings[i]
for i in range(N):
    if word in rings[i]:
        result += 1
print(result)