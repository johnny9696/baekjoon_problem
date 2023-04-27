"""
처음 물병에는 모두 1리터 들어 있음
N개의 물병 한번에 K개 이동 가능함
"""
import sys
N, K   = map(int,input().split())
count = 0
while bin(N).count('1') > K:
    N += 1
    count += 1
print(count)
