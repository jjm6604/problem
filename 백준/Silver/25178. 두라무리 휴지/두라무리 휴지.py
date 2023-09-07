lst = ['a', 'e', 'i', 'o', 'u']
N = int(input())
word1 = input()
word2 = input()
w1 = ''
w2 = ''
l1 = []
l2 = []
for i in range(N):
    if word1[i] not in lst:
        w1 += word1[i]
    else:
        l1.append(word1[i])
    if word2[i] not in lst:
        w2 += word2[i]
    else:
        l2.append(word2[i])
l1.sort()
l2.sort()
if w1 == w2 and l1 == l2 and word1[0] == word2[0] and word1[-1] == word2[-1]:
    print('YES')
else:
    print('NO')
