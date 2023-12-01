import sys
from collections import deque

input = sys.stdin.readline



N = int(input())

result = 0
r_pos = []

for i in range(N):
    L = int(input())
    jew = list(map(int,input().split()))
    mx = jew[0]
    mx_start = mx_end = 0
    start = end = 0
    for i in range(1,L):
        if jew[i] >= jew[i-1] + jew[i]:
            start = i
            end = i
        else:
            jew[i] = jew[i-1] + jew[i]
            end = i

        if jew[i] > mx:
            mx = jew[i]
            mx_end = end
            mx_start = start
        elif jew[i] == mx and mx_end-mx_start > end - start:
            mx = jew[i]
            mx_end = end
            mx_start = start

    result += mx
    r_pos.append((mx_start+1,mx_end+1))

print(result)
for i in range(len(r_pos)):
    print('{} {}'.format(r_pos[i][0], r_pos[i][1]))