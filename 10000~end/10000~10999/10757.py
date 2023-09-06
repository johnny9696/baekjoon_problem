def sum_one_digit(a,b,c):
    c=int(a)+int(b)+int(c)
    if c>=10:
        c=[c//10,c%10]
    else:
        c=[0,c]
    return c

a,b=input().split()
"""
print(type(a),type(b))
print(len(a),len(b))
c=str(1)
print(c)
c=c+'2'
print(c)
"""
a_c=len(a)-1
b_c=len(b)-1
c=[0,0]
result=str()
if(a_c>b_c):
    big_size=a_c
else:
    big_size=b_c

for i in range(0,big_size+1):
    if(a_c<0):
        a_in=0
    else:
        a_in=a[a_c]
        a_c=a_c-1
    if(b_c<0):
        b_in=0
    else:
        b_in=b[b_c]
        b_c=b_c-1
    c=sum_one_digit(a_in,b_in,c[0])
    result=str(c[1])+result
    #print(result)
if(c[0]!=0):
    result=str(c[0])+result
print(result)




