def solution(wallet, bill):
    answer = 0
    l_wallet = max(wallet)
    s_wallet = min(wallet)
    
    while True:
        l_bill = max(bill)
        s_bill = min(bill)
        if l_wallet >= l_bill and s_wallet >= s_bill:
            break
        bill = [s_bill, l_bill // 2]
        answer += 1
        
    return answer