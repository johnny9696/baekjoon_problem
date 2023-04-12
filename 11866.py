from collections import deque

n, k = map(int,input().split())
q = deque()
for i in range(1,n+1):
    q.append(i)
count = 0
result= []
while q:
    t = q.popleft()
    count +=1
    if count == k:
        count = 0
        result.append(t)
    else:
        q.append(t)

print("<",end ='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(str(result[-1])+">")


