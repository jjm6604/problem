doc = input()
word = input()
cnt = 0
i = 0
while i <= len(doc) - len(word):
    if word == doc[i:i+len(word)]:
        cnt += 1
        i += len(word)
    else:
        i += 1
print(cnt)