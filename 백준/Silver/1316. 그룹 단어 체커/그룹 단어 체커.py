n = int(input())
count = 0
for i in range(0, n):
    my_list = [0] * 26
    my_str = input()

    my_list[ord(my_str[0])-97] += 1
    for j in range(1, len(my_str)):
        if (my_str[j] == my_str[j-1]) :
            continue
        my_list[ord(my_str[j])-97] += 1

    for j in range(len(my_list)):
        if my_list[j] >= 2:
            break
        if j == 25:
            count += 1

print(count)
