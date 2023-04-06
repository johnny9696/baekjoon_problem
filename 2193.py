n = int(input())

if n == 1 or n ==2:
    print(1)
else:
    n_list = [1 for _ in range(n+1)]
    for i in range(3, n+1):
        n_list[i] = n_list[i-2] + n_list[i-1]
    print(n_list[-1])