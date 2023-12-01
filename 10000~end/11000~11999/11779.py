import sys

input = sys.stdin.readline
print = sys.stdout.write

city = int(input())
bus = int(input())
near_list = [[] for _ in range(city + 1)]

for _ in range(bus):
    sp, ep, time = map(int, input().split())
    near_list[sp].append((ep, time))

visited = [False] * (city + 1)
sp, ep = map(int, input().split())

def DFS(x):
    if x == ep:
        return [ep], 0
    else:
        result = []
        tmp_cost = sys.maxsize
        for next in near_list[x]:
            next_p = next[0]
            t_cost = next[1]
            if not visited[next_p]:
                visited[next_p] = True
                tmp_list, tmp_time = DFS(next_p)
                visited[next_p] = False
                if tmp_time + t_cost < tmp_cost:
                    result = tmp_list
                    tmp_cost = tmp_time + t_cost
        return [x] + result, tmp_cost


visited[sp] = True
result, cost = DFS(sp)
print(str(cost)+'\n')
print(str(len(result))+'\n')
for i in result:
    print(str(i) + ' ')