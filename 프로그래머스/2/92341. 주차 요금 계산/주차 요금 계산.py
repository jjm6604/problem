def solution(fees, records):
    answer = []
    car_lst = []
    car_dict = {}
    time_dict = {}
    in_lst = []
    
    for record in records:
        time, car, action = record.split()
        if action == 'IN':
            car_dict[car] = time
            in_lst.append(car)
            if car not in car_lst:
                car_lst.append(car)
        else:
            in_lst.pop(in_lst.index(car))
            h1, m1 = map(int, time.split(':'))
            h2, m2 = map(int, car_dict[car].split(':'))
            minutes = m1 - m2 + (h1 - h2) * 60
            time_dict[car] = time_dict.get(car, 0) + minutes

    for i in in_lst:
        h, m = map(int, car_dict[i].split(':'))
        minutes = 59 - m + (23 - h) * 60
        time_dict[i] = time_dict.get(i, 0) + minutes
        
    car_lst.sort()
    
    for c in car_lst:
        total = time_dict[c]
        fee = fees[1]
        if total > fees[0]:
            fee += ((total - fees[0]) // fees[2]) * fees[3]
            if (total - fees[0]) % fees[2]:
                fee += fees[3]
        answer.append(fee)
        
    return answer