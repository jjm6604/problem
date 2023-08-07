while True:
    my_str = input()

    if my_str == '.':
        break

    lst = []
    result = 'yes'
    for s in my_str:
        if s == '[':
            lst.append(']')
        if s == '(':
            lst.append(')')
        elif s == ']' or s == ')':
            if len(lst) == 0:
                result = 'no'
                break
            char = lst.pop()
            if char != s:
                result = 'no'
                break

    if len(lst) != 0:
        result = 'no'
    print(result)