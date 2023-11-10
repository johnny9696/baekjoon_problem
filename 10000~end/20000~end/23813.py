n = int(input())
tmp = 0
cnt = 0
while n >0 :
    cnt += 1
    tmp += n % 10
    n = n//10

result = 0
for i in range(cnt):
    result += (tmp * (10 ** i))
print(result)