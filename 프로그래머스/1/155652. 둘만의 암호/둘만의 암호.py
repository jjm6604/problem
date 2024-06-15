def solution(s, skip, index):
    answer = ''
    skip_lst = []
    for skip_word in skip:
        skip_lst.append(ord(skip_word))
    for word in s:
        word_num = ord(word)
        i = 0
        while i < index:
            word_num += 1
            if word_num > 122:
                word_num -= 26
            if word_num in skip_lst:
                continue
            i += 1

        answer += chr(word_num)            
        
    return answer