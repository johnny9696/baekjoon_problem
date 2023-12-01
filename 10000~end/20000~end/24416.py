def fib(n):
    fibo = [1 for _ in range(n+1)]
    for i in range(3, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]

n = int(input())

print(fib(n), n-2)