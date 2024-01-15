def backtrack(n, new_word):
    if n >= 2 and new_word[n-2] == new_word[n-1]:
        return
    if n == length:
        res.add(new_word)
        return
    for i in range(length):
        if checked[i] == 0:
            checked[i] = 1
            backtrack(n+1, new_word + word[i])
            checked[i] = 0

            
word = input()
length = len(word)
checked = [0] * length
res = set()
backtrack(0, '')
print(len(res))