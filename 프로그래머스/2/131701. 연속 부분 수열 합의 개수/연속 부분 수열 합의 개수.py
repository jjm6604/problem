def solution(elements):
    N = len(elements)
    sums = set()
    sums.add(sum(elements))
    elements += elements[:]
    for i in range(N):
        for j in range(1, N):
            sums.add(sum(elements[i:i + j]))
    answer = len(sums)
    return answer