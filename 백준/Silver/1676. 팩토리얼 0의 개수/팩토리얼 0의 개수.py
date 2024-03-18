N = int(input())

num = 1
res = 0
for i in range(2, N+1):
    num *= i

while True:
    if num % 10 == 0:
        res += 1
        num //= 10
    else:
        break
print(res)