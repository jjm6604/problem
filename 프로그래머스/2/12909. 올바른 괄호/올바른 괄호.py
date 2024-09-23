def solution(s):
    
    lst = []
    
    for i in s:
        if i == '(':
            lst.append(0)
        else:
            if lst:
                lst.pop()
            else:
                return False
    
    if lst:
        return False

    return True