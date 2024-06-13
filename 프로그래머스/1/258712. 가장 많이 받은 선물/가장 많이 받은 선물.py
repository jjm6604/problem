def solution(friends, gifts):
    answer = 0
    friend_score = {}
    gift_count = [0] * len(friends)
    for friend in friends:
        friend_score[friend] = 0
    for gift in gifts:
        A, B = gift.split()
        friend_score[A] += 1
        friend_score[B] -= 1
        
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            cnt_A, cnt_B = gifts.count(f'{friends[i]} {friends[j]}'), gifts.count(f'{friends[j]} {friends[i]}')
            if cnt_A > cnt_B:
                gift_count[i] += 1
            elif cnt_A < cnt_B:
                gift_count[j] += 1
            else:
                if friend_score[friends[i]] > friend_score[friends[j]]:
                    gift_count[i] += 1
                elif friend_score[friends[i]] < friend_score[friends[j]]:
                    gift_count[j] += 1
    answer = max(gift_count)
    return answer