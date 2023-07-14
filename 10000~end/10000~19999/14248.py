import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

n_rocks = list(map(int,input().split()))
visited = [False] * n
sp = int(input())
np =deque()
np.append(sp-1)
result = 1
visited[sp-1] = True

move = [-1,1]
while np:
    sp = np.popleft()
    for i in move:
        next_p = sp + n_rocks[sp] * i
        if 0<= next_p< n:
            if not visited[next_p]:
                result+=1
                visited[next_p] = True
                np.append(next_p)
print(result)

