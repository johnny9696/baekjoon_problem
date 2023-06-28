import sys
input = sys.stdin.readline

T = int(input())
fibo = [1] * 10001
for i in range(3,10001):
    fibo[i] = fibo[i-1] + fibo[i-2]
for i in range(1,T+1):
    P,Q = map(int,input().split())
    print('Case #{}: {}'.format(i,fibo[P]%Q))