T = int(input())
for t in range(T):
    coord = list(map(int, input().split()))
    size = (coord[3] - coord[1]) * (coord[2] - coord[0])
    size -= max(0, (min(coord[3], coord[7]) - (max(coord[1],coord[5])))) * max(0, (min(coord[2], coord[6]) - max(coord[0],coord[4])))
    print(size)