import sys
input = sys.stdin.readline

n = int(input())
max_effort = [0] * (n+10)

for now in range(1, n+1):
    length, effort = map(int,input().split())
    if now + length - 1 <= n:
        max_effort[now+length-1]=max(max(max_effort[:now]) + effort, max_effort[now + length - 1])

print(max(max_effort))
