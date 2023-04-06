import sys
n = int(input())

c_list = [sys.maxsize] * (n+1)
c_list[n] = 0
cnt = 0
for i in range(n, 1, -1):
    if i%3 == 0 :
        c_list[i//3] = min(c_list[i//3],c_list[i] + 1)
    if i%2 == 0 :
        c_list[i // 2] =min(c_list[i//2],c_list[i] + 1)
    c_list[i-1]= min(c_list[i-1],c_list[i] + 1)
print(c_list[1])