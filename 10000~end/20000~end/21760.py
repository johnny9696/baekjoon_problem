n,m,k = map(int,input().split())

t1 = 1
t2 = 0
t3 = 0
t4 = 0
for i in range(1,n+1):
    t1 = t1*i
    if i == m:
        t2 = t1
    if i == n-k:
        t3 = t1
    if i == m-k:
        t4 = t1
print((t3*t2)/(t1*t4))