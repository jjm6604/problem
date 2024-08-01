def solution(sequence, k):
    answer = []
    length = float('inf')
    number = sequence[0]
    N = len(sequence)
    i, j = 0, 0
    while True:
        if number == k:
            if length > (j - i):
                length = j - i
                answer = [i, j]
        if number < k:
            if j == N - 1:
                break
            j += 1
            number += sequence[j]
        else:
            number -= sequence[i]
            i += 1

    
    return answer