n = int(input())

fibo= [0,1]
for i in range(1, n):
    fibo.append((fibo[i-1]+fibo[i])%1000000007)
print(fibo[n])