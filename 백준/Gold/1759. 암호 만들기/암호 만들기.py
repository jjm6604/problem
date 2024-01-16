def backtrack(n, m, password):
    if n == L:
        cnt = 0
        for w in ['a', 'e', 'i', 'o', 'u']:
            if w in password:
                cnt += 1
        if cnt >= 1 and L - cnt >= 2:
            print(password)
        return
    if L - n > C - m:
        return
    backtrack(n+1, m+1, password + lst[m])
    backtrack(n, m+1, password)


L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
checked = [0] * C
backtrack(0, 0, '')