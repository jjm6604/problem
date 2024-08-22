def solution(s):
    answer = 0

    
    N = len(s)
    for i in range(N):
        word = s[i:] + s[:i]
        lst = []
        for j in range(N):
            if word[j] == '[':
                lst.append('[')
            elif word[j] == '(':
                lst.append('(')
            elif word[j] == '{':
                lst.append('{')
            else:
                if not lst:
                    break
                elif word[j] == ']':
                    if lst.pop() != '[':
                        break
                elif word[j] == ')':
                    if lst.pop() != '(':
                        break
                elif word[j] == '}':
                    if lst.pop() != '{':
                        break
        else:
            if not lst:
                answer += 1
                
    
    return answer