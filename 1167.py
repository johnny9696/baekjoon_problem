n, m  = map(int, input().split())
s = 0
e = n
n_list = list(map(int,input().split()))
for i in n_list:
    if s<i:
        s= i
    e += i

while s<=e:
    middle = (s+e)//2
    sum = 0
    count = 0
    for i in range(n):
        if sum + n_list[i] > middle:
            count +=1
            sum =0
        sum += n_list[i]
    if sum!=0:
        count +=1
    if  count>m:
        s = middle +1
    else:
        e= middle -1
print(s)