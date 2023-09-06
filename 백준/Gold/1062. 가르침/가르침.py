import sys

def select_char(n, cnt):
    if cnt == need_cnt:
        select_lst.append(list(char)[:])
        return
    if n >= len(need_char):
        return
    char.add(need_char[n])
    select_char(n+1, cnt+1)
    char.remove(need_char[n])
    select_char(n+1, cnt)

N, K = map(int, sys.stdin.readline().strip().split())
words = [sys.stdin.readline().strip() for _ in range(N)]
char = {'a', 'n', 't', 'i', 'c'}
need_char = set()
need_cnt = K - 5
if need_cnt < 0:
    print(0)
    exit(0)
else:
    for word in words:
        for w in word:
            if w not in char:
                need_char.add(w)
    need_char = list(need_char)
    if len(need_char) < need_cnt:
        print(len(words))
        exit(0)
    select_lst = []
    select_char(0, 0)
    result = 0
    for select in select_lst:
        result_cnt = 0
        for word in words:
            word_cnt = 1
            for w in word:
                if w not in select:
                    word_cnt = 0
                    break
            result_cnt += word_cnt
        if result < result_cnt:
            result = result_cnt
    print(result)