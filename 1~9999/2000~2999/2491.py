import sys
from collections import deque

input = sys.stdin.readline

length = int(input())
n_list = list(map(int,input().split()))

bigger = 1
smaller = 1
tmpbigger = 1
tmpsmaller = 1
for i in range(1,len(n_list)):
    if n_list[i-1] < n_list[i]:
        tmpbigger += 1
        tmpsmaller = 1
    elif n_list[i-1] == n_list[i]:
        tmpbigger +=1
        tmpsmaller +=1
    else:
        tmpbigger = 1
        tmpsmaller +=1
    bigger = max(bigger,tmpbigger)
    smaller = max(smaller,tmpsmaller)

result = max(bigger,smaller)

print(result)