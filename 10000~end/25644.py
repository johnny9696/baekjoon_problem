import sys
input = sys.stdin.readline
days = int(input())
price = list(map(int,input().split()))
max_price = 0
max_effort = 0
for i in range(len(price)-1,-1,-1):
    max_price = max(max_price,price[i])
    max_effort = max(max_effort,max_price-price[i])
print(max_effort)