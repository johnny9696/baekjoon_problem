import sys
input = sys.stdin.readline
N,K =map(int,input().split())
temp_list = list(map(int,input().split()))
max_temp = sum(temp_list[:K])
now = max_temp
for i in range(K, N):
    now = now + temp_list[i] - temp_list[i-K]
    max_temp = max(max_temp, now)
print(max_temp)