s,k=map(int,input().split())
head=s//k
print(head)
remain=s%k
print(remain)
result=1
for i in range(0,k):
    if i<remain:
        result=result*(head+1)
    else:
        result=result*head
    print(result)
print(result)