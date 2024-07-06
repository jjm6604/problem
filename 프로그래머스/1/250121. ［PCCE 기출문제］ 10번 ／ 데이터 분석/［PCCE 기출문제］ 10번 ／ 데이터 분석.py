def solution(data, ext, val_ext, sort_by):
    answer = []
    idx = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    n = idx[ext]
    k = idx[sort_by]
    for d in data:
        if d[n] < val_ext:
            answer.append(d)
    answer.sort(key = lambda x: x[k])
    return answer