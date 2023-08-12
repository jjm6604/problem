game = [0, 'SK', 'CY', 'SK', 'SK']
N = int(input())
for i in range(5, N+1):
    if game[i-1] == 'CY' or game[i-3] == 'CY' or game[i-4] == 'CY':
        game.append('SK')
    else:
        game.append('CY')
        
print(game[N])