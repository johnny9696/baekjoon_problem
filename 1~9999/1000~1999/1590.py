"""
N T
S I C
"""
import sys
N, T = map(int,input().split())
min_wait = sys.maxsize
for i in range(N):
    S, I, C = map(int,input().split())
    can = False
    for i in range(C):
        if T <= S:
            can = True
            break
        S += I
    if can:
        min_wait = min(min_wait, S-T)
if min_wait == sys.maxsize:
    print(-1)
else:
    print(min_wait)