from math import factorial

n = int(input())

fact_list = [factorial(i) for i in range(21) if factorial(i) <= n]
isFact = False
while n > 0:
    fact_list = list(filter(lambda x: x <=n, fact_list))
    if len(fact_list) == 0:
        break
    n -= fact_list.pop()
    if n <= 0:
        if n == 0:
            isFact = True
        break
print('YES' if isFact else 'NO')