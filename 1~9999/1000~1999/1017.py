import sys
sys.setrecursionlimit(10**6)

n = int(input())

n_list = list(map(int,input().split()))

sosu = [True] * 2001
sosu[0] = False
sosu[1] = False
for i in range(2, 2001):
    if sosu[i] == True:
        cnt = 2
        while i*cnt <=2000:
            sosu[i * cnt] = False
            cnt+=1

visited = [False] * n
result = []

def DFS(now, depth):

    for i in range(n):
        if not visited[i]:
            if sosu[now + i]:
                visited[i] = True
                for j in range(n):
                    if not visited[j]:
                        DFS(j, depth + 1)

