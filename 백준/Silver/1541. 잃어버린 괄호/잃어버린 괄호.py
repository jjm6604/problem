nums = input()
nums += '+'
N = len(nums)
number = ''
flag = False
answer = 0

for i in range(N):
    if '0' <= nums[i] <= '9':
        number += nums[i]
    else:
        if nums[i] == '-':
            if flag:
                answer -= int(number)
            else:
                answer += int(number)
                flag = True
            number = ''
        else:
            if flag:
                answer -= int(number)
            else:
                answer += int(number)
            number = ''

print(answer)
