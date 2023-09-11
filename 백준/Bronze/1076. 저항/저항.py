color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

color_lst = [input() for _ in range(3)]

num1 = color.index(color_lst[0])
num2 = color.index(color_lst[1])
num3 = color.index(color_lst[2])
num = int(str(num1) + str(num2))
num *= (10 ** num3)
print(num)