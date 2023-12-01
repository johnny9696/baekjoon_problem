import sys

input = sys.stdin.readline

while True:
    days = int(input())
    if days == 0:
        break
    n_profit = [int(input()) for _ in range(days)]
    for i in range(1, days):
        n_profit[i] = max(n_profit[i], n_profit[i]+n_profit[i-1])
    print(max(n_profit))