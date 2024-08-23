from collections import deque

def solution(begin, target, words):
    answer = 0
    N = len(begin)
    checked = set()
    
    q = deque()
    q.append([begin, 0])
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in range(N):
            if word[i] != target[i]:
                for j in range(26):
                    new_word = word[:i] + chr(97 + j) + word[i+1:]
                    if new_word in words and new_word not in checked:
                        q.append([new_word, cnt + 1])
                        checked.add(new_word)
                
    return answer