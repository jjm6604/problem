flag = True
answer = 0

def solution(word):
    def backtrack(aeiou):
        global flag, answer
        if flag:
            if aeiou == word:
                flag = False
                return
            answer += 1
            if len(aeiou) == 5:
                return
            for i in ['A', 'E', 'I', 'O', 'U']:
                backtrack(aeiou + i)

    backtrack('')    
    return answer
