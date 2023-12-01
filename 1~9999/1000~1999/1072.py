"""
z=y+t/x+t
zx+zt = (y + t)*100
(z-100)t= y*100-zx
t = (y*100-zx)/(z-100)
"""
import math
x,y = map(int,input().split())
z = (y*100)//x

if z == 100 or z == 99:
    print(-1)
else:
    z = z+1
    t = (y*100-z*x)/(z-100)
    print(math.ceil(t))