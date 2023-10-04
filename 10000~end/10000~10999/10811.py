n, m = map(int,input().split())
bucket = [i for  i in range(0, n+1)]

for i_ in range(m):
    a,b= map(int,input().split())
    tmp = bucket[a:b+1]
    tmp.reverse()
    bucket[a:b+1] = tmp
for i in range(1, n+1):
    print(bucket[i], end = ' ')