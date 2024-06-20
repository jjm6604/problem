def solution(new_id):
    answer = ''
    change = ''
    for id in new_id:
        if 65 <= ord(id) < 90:
            change += chr(ord(id) + 32)
        else:
            change += id
    new_id = change
    change = ''
    
    for id in new_id:
        if 97 <= ord(id) <= 122 or 48 <= ord(id) <= 57 or id == '-' or id == '_' or id == '.' :
            change += id
    
    
    new_id = change
    change = new_id[0]
    
    for i in range(1, len(new_id)):
        if change[-1] == '.' and new_id[i] == '.':
            continue
        else:
            change += new_id[i]
    
    new_id = change
    while (new_id and new_id[0] == '.'):
            new_id = new_id[1:]
    while (new_id and new_id[-1] == '.'):
        new_id = new_id[:-1]
    if new_id == '':
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
        while (new_id[0] == '.'):
            new_id = new_id[1:]
        while (new_id[-1] == '.'):
            new_id = new_id[:-1]
    while (len(new_id) <= 2):
        new_id += new_id[-1]
    
    answer = new_id
        
            
    return answer