n,m = map(int,input().split())

if n < m:
    print(1)
elif n == m:
    print(2)
else:
    combi = [1 for _ in range(n+1)]
    combi[m] = 2

    for time in range(m+1, n+1):
        combi[time]= (combi[time-1] + combi[time - m]) % 1000000007
    print(combi[-1])