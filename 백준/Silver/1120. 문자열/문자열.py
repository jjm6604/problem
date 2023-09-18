word1, word2 = input().split()

min_value = float("inf")
for i in range(len(word2)-len(word1)+1):
    value = 0
    for j in range(len(word1)):
        if word1[j] != word2[i+j]:
            value += 1
    if min_value > value:
        min_value = value
print(min_value)