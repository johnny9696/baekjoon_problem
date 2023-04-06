from math import *
num=int(input())
i=0
result=str()
while num>=2**(i+1):
    i+=1
    num=num-2**i
if(num==0):
    print(str(7)*i)
else:

