T = int(input())
cnt = 0
for t in range(T):
    s = []
    result = 1
    word = input()
    s.append(word[0])
    for i in range(1, len(word)):
        if len(s) > 0:
            n = s.pop()
            if word[i] != n:
                s.append(n)
                s.append(word[i])
        else:
            s.append(word[i])
    if len(s) != 0:
        result = 0
    cnt += result
print(cnt)
