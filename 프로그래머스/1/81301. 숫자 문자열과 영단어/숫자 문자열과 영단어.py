def solution(s):
    answer = ''
    numbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    N = len(s)
    i = 0
    number = '0123456789'
    word = ''
    while True:
        if i == N:
            break
        if s[i] not in number:
            word += s[i]
            if word in list(numbers.keys()):
                answer += numbers[word]
                word = ''
                
        else:
            answer += s[i]
        i += 1
    answer = int(answer)
    return answer