n, l = map(int,input().split())

#l은 2~100 사이
result = []
for i in range(l, 101):
    #짝수 일떄
    if i % 2 == 0:
        k = i//2
        if (n+k)%i == 0 and (n+k)/i >= k:
            m = (n+k)//i
            for j in range(-k,k):
                result.append(str(m+j))
            break
    #홀수 일때
    else:
       k = (i-1)//2
       if n%(2*k+1)==0 and n/(2*k+1) >= k:
           m = n//(2*k+1)
           for j in range(-k,k+1):
               result.append(str(m+j))
           break
if len(result) == 0:
    print(-1)
else:
    result = " ".join(result)
    print(result)