T = int(input())

for t in range(T):
    words = list(input().split())
    res = ''
    for word in words:
        new_word = ''
        for i in range(len(word)-1, -1, -1):
            new_word += word[i]
        res += new_word + ' '
    print(res)
