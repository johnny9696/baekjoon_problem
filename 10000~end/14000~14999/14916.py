n = int(input())

result_5 = n // 5
n = n % 5
result_2 = 0
if n % 2 == 0:
    result_2 = n // 2
    n = n % 2
else:
    if result_5 > 0 :
        result_5 += -1
        n += 5
        result_2 = n // 2
        n = n % 2
if n != 0:
    print(-1)
else:
    print(result_5 + result_2)