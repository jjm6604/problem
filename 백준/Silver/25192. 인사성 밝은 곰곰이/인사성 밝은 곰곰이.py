import sys
N = int(sys.stdin.readline())
cnt = 0
check = set()
for i in range(N):
    name = sys.stdin.readline().strip()
    if name == 'ENTER':
        cnt += len(check)
        check.clear()
    else:
        check.add(name)
cnt += len(check)
print(cnt)