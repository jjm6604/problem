word = input()
a = word.count('a')
word *= 2
n = len(word)
answer = set()
for i in range(n):
    answer.add(word[i:i+a].count('a'))

print(a - max(answer))