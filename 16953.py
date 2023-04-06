a, b = map(int, input().split())
depth = 1
while a<b:
    if b%10 ==1:
        b=b//10
        depth +=1
    else:
        if b%2 == 0:
            b= b//2
        else:
            break
        depth +=1
if a==b:
    print(depth)
else:
    print(-1)