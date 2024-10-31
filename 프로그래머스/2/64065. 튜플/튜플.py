def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    N = len(s)
    numbers = [[] for _ in range(N)]

    for i in s:
        lst = list(map(int, i.split(',')))
        n = len(lst) - 1
        numbers[n] = lst
        
    for number in numbers:
        for num in number:
            if num not in answer:
                answer.append(num)
                break
                
    return answer