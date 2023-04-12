import sys
input = sys.stdin.readline

n,m = map(int, input().split())

data = list(map(int, input().split()))
result = 0

t_data=[0 for _ in range(m)]
temp =0
for i in data:
    temp += i
    remain = temp % m
    if remain ==0 :
        result += 1
    t_data[remain] += 1

for i in t_data:
    if i >1 :
        result += i*(i-1)//2
print(result)