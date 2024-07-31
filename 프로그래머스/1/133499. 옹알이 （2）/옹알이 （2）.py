speak = ['aya', 'ye', 'woo', 'ma']
def solution(babbling):
    answer = 0
    for b in babbling:
        word = ''
        idx = -1
        for i in range(len(b)):
            word += b[i]
            if word in speak and idx != speak.index(word):
                idx = speak.index(word)
                word = ''
                
                
        if not word:
            answer += 1
                
    return answer