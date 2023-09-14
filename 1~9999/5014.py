import sys
from collections import deque

input = sys.stdin.readline

F,S,G,U,D = map(int,input().split())
move = [U,-D]
cnt = [sys.maxsize] * (F+1)
def BFS(s):
    dp = deque ()
    dp.append(s)

    cnt [s] = 0
    while dp:
        now = dp.popleft()
        for i in move:
            if 0< now + i <=F:
                if cnt[now] + 1 < cnt[now+i]:
                    cnt[now + i] = min(cnt[now] + 1, cnt[now + i])
                    dp.append(now + i)
            if now + i == G:
                return

BFS(S)
if cnt[G] != sys.maxsize:
    print(cnt[G])
else:
    print('use the stairs')