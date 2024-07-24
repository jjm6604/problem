def solution(players, callings):
    player_dict = {}
    for i in range(len(players)):
        player_dict[players[i]] = i 
    for calling in callings:
        idx = player_dict[calling]
        player_dict[calling] = idx - 1
        player_dict[players[idx - 1]] += 1
        players[idx], players[idx-1] = players[idx-1], players[idx]
    answer = players
    return answer