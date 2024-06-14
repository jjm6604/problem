def solution(bandage, health, attacks):
    answer = 0
    i = 0
    time = 0
    max_health = health
    bandage_time = 0
    while True:
        time += 1

        if attacks[i][0] == time:
            bandage_time = 0
            health -= attacks[i][1]
            i += 1
            if health <= 0:
                answer = -1
                break
        else:
            bandage_time += 1
            bandage_health = health + bandage[1]
            if bandage_time == bandage[0]:
                bandage_time = 0
                bandage_health += bandage[2]
            health = min(max_health, bandage_health)
        if i == len(attacks):
            answer = health
            break
    return answer