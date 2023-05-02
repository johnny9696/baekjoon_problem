a, b= map(int,input().split())
if a>b:
    a,b= b,a
while b%a!=0:
    a,b = b%a, a

result = '1'*a


print(result)