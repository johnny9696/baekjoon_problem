import sys

input = sys.stdin.readline

while True:
    try:
        n_list = list(map(float, input().split()))
        point = []
        for i in range(0, 4):
            if [n_list[i * 2], n_list[i * 2 + 1]] not in point:
                point.append([n_list[i * 2], n_list[i * 2 + 1]])
            else:
                bp = [n_list[i * 2], n_list[i * 2 + 1]]
        v =[]
        for i in point:
            if i != bp:
                v.append([i[0]-bp[0],i[1]-bp[1]])
        result = bp
        for i in v:
            result[0] += i[0]
            result[1] += i[1]

        print("{:.3f} {:.3f}".format(result[0], result[1]))
    except:
        break

