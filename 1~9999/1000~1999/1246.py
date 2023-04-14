"""
달걀 갯수N 고객 M
i 번째 고객 P이하로 구매 가능
1개씩만 팜
책정 가격 올릴 수 있는 수입 계산
"""
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
price_list = [int(input()) for _ in range(M)]
price_list.sort(reverse=True)
max_val = 0
for i, n_price in enumerate(price_list):
    if i+1 <N:
        t = n_price * (i+1)
    else:
        t = n_price * N
    if t>max_val:
        max_val = t
        max_price=n_price
print(max_price,max_val)
