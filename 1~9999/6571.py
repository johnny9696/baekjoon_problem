fibo = [1,1]

while fibo[-1] < 10 ** 100:
    fibo.append(fibo[-1]+fibo[-2])

while True:
    a,b = map(int,input().split())
    if a== 0 and b == 0:
        break
    result = 0
    for i in fibo[1:]:
        if a<= i <=b:
            result+=1
    print(result)