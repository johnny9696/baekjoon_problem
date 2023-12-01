import sys

input = sys.stdin.readline

n = int(input())

n_list = []
for _ in range(n):
    n_list.append(list(map(int,input().split())))

n_dist = []
def man_dist(point):
    x1 , y1 = n_list[point][0], n_list[point][1]
    x2 , y2 = n_list[point + 1][0], n_list[point + 1][1]
    x3,  y3 = n_list[point + 2][0], n_list[point + 2][1]
    n_dist.append((abs(x1-x2) + abs(y1-y2), abs(x1-x3) + abs(y1-y3)))
    return n_dist[point][1] - n_dist[point][0] - (abs(x2-x3)+abs(y2-y3))

min_dist = sys.maxsize
min_point = None

for i in range(n-2):
    gap = man_dist(i)
    if gap < min_dist:
        min_point = i
        min_dist = gap

n_dist.append([abs(n_list[n-2][0]-n_list[n-1][0])+abs(n_list[n-2][1]-n_list[n-1][1]), None])

result = 0
for i in range(n-1):
    if i != min_point:
        result += n_dist[i][0]
    else:
        result += n_dist[i][1]
        result -= n_dist[i+1][0]
print(result)