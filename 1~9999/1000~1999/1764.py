import sys
input = sys.stdin.readline
n, m = map(int,input().split())
non=set()
for i in range(n):
    non.add(input())
hear = set()
for j in range(m):
    hear.add(input())
result = sorted(list(non&hear))
print(len(result))
for i in result:
    print(i, end='')