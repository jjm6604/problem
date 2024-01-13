def backtrack(n, num):
    if n == length:
        if int(num) > int(X):
            nums.add(int(num))
        return

    for i in range(length):
        if selected[i] == 0:
            selected[i] = 1
            backtrack(n+1, num + X[i])
            selected[i] = 0

            
X = input()
length = len(X)
selected = [0] * length
nums = set()

backtrack(0, '')
if nums:
    print(min(nums))
else:
    print(0)