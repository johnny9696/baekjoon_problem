import sys

input = sys.stdin.readline

n = int(input())
price_list = list(map(int,input().split()))

max_price = [0 for _ in range(n + 1)]

for i in range(1,n+1):
    tmp = [max_price[j] + price_list[i-j-1] for j in range(i)]
    max_price[i] = max(tmp)
print(max_price[-1])