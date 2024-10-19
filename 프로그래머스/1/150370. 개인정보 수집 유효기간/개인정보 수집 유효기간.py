def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    for term in terms:
        x, month = term.split()
        term_dict[x] = int(month)
    
    for i in range(len(privacies)):
        day, x = privacies[i].split()
        before = list(map(int, day.split('.')))
        now = list(map(int, today.split('.')))
        
        time = 0
        
        time += (now[0] - before[0]) * 12 + (now[1] - before[1])
        if now[2] - before[2] < 0:
            time -= 0.5
        
        if term_dict[x] <= time:
            answer.append(i + 1)
        
    return answer