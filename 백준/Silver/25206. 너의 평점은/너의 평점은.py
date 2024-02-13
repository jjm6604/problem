total_score = 0

sum = 0
for i in range(0, 20):

    my_str = input()
    str_list = my_str.split()
    score = str_list[2][0]
    score_sum = float(str_list[1])
    if(score != 'P'):
        sum += score_sum
        if(score == 'A'):
            total_score += score_sum * 4
        elif(score == 'B'):
            total_score += score_sum * 3
        elif(score == 'C'):
            total_score += score_sum * 2
        elif (score == 'D'):
            total_score += score_sum * 1

        if(score != 'F' and str_list[2][1] == '+'):
            total_score += score_sum * 0.5

final_score = total_score / sum
print(final_score)