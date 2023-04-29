import sys
input = sys.stdin.readline
N,K =map(int,input().split())
temp_list = list(map(int,input().split()))
max_temp = -sys.maxsize

for i in range(K, N):
    max_temp = max(max_temp, sum(temp_list[-K+i:i]))
print(max_temp)