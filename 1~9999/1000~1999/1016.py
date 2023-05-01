import math
min_num, max_num= map(int,input().split())
check = [False] * (max_num-min_num+1)

for i in range(2, int(math.sqrt(max_num)+1)):
    pow = i*i
    start_index= int(min_num/pow)
    if min_num%pow!=0:
        start_index+=1
    for j in range(start_index,int(max_num/pow+1)):
        check[int((j*pow)-min_num)] = True
count = 0
for i in range(len(check)):
    if not check[i]:
        count +=1
print(count)
