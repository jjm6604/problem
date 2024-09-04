def solution(sequence):
    answer = 0
    
    
    N = len(sequence)
    numbers = [[0] * N for _ in range(2)]
    numbers[0][0] = max(0, sequence[0])
    numbers[1][0] = max(0, -sequence[0])

    for i in range(1, N):
        for j in range(2):
            if (i + j) % 2 == 0:
                numbers[j][i] = max(0, numbers[j][i-1] + sequence[i])
            else:
                numbers[j][i] = max(0, numbers[j][i-1] - sequence[i])
                
    answer = max(max(numbers[0]), max(numbers[1]))
    
    
    return answer