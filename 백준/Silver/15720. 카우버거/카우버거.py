n_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
s_lst = list(map(int, input().split()))
w_lst = list(map(int, input().split()))

b_lst.sort(reverse=True)
s_lst.sort(reverse=True)
w_lst.sort(reverse=True)

min_value = min(n_lst)
before_result = sum(b_lst) + sum(s_lst) + sum(w_lst)
for i in range(min_value):
    b_lst[i] = b_lst[i] * 0.9
    s_lst[i] = s_lst[i] * 0.9
    w_lst[i] = w_lst[i] * 0.9

result = sum(b_lst) + sum(s_lst) + sum(w_lst)
print(before_result)
print(int(result))