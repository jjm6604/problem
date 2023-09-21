N = int(input())
words = [input() for _ in range(N)]
lst = [[] for _ in range(51)]
words = list(set(words))
for word in words:
    lst[len(word)].append(word)

for l in lst:
    l.sort()
    for i in l:
        print(i)