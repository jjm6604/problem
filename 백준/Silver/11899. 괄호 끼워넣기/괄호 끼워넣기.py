word = input()
cnt = 0
s = []
for i in range(len(word)):
    if word[i] == '(':
        s.append(1)
    else:
        if s:
            s.pop()
        else:
            cnt += 1
cnt += len(s)
print(cnt)