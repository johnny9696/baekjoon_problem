import sys

input = sys.stdin.readline

n, m = map(int, input().split())
chicken = []
house = []
for i in range(n):
    tmp_list = list(map(int, input().split()))
    for j in range(n):
        if tmp_list[j] == 1:
            house.append([i, j])
        elif tmp_list[j] == 2:
            chicken.append([i, j])


while len(chicken) >= m:
    house_l = [[sys.maxsize, sys.maxsize] for _ in range(len(house))]
    chicken_c = [0] * len(chicken)
    for i in range(len(house)):
        for j in range(len(chicken)):
            dist = abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1])
            b_dist = house_l[i][1]
            if dist < b_dist:
                if house_l[i][0] == sys.maxsize:
                    house_l[i] = [j, dist]
                    chicken_c[j] += 1
                else:
                    chicken_c[house_l[i][0]] -= 1
                    chicken_c[j] += 1
                    house_l[i] = [j, dist]
    t = min(chicken_c)
    indx = chicken_c.index(t)
    chicken.pop(indx)
result = 0
for i in house_l:
    result += i[1]
print(result)

