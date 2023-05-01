import sys
input =sys.stdin.readline()
n = int(input())
result = [0 for x in range(10001)]
for i in range(n):
    result[int(input())] += 1
for i, j in enumerate(result):
    if i != 0:
        for k in range(j):
            print(i)
