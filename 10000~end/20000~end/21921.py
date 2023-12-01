import sys
input = sys.stdin.readline

N,X = map(int,input().split())
data = list(map(int,input().split()))

if max(data) == 0:
    print('SAD')
else:
    max_value = sum(data[:X])
    value = max_value
    cnt = 1

    for i in range(X,N):
        value = value + data[i] - data[i-X]

        if value > max_value:
            cnt = 1
            max_value = value
        elif value == max_value:
            cnt += 1
    print(max_value)
    print(cnt)