n = int(input())
k = int(input())
s_num =[00]
for i in range(1, n):
    s_num.append(s_num[i-1]+i)
for i in range(n,0,-1):
    s_num.append(s_num[-1]+i)
s= 1
e= len(s_num)
while s!=e:
    middle= (s+e)//2
    if s_num[middle] ==k:
        break
    elif s_num[middle]>k:
        e = middle-1
    else:
        s= middle+1

