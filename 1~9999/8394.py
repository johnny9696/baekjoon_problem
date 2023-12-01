n = int(input())

a,b,c = 0,1,2
for i in range(n-2):
    a,b,c = b,c, (b+c)%10

print(c)