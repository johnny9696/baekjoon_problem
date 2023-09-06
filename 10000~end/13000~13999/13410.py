def num_reverse(x):
    result = 0
    while x//10 !=0 or x % 10 != 0:
        result = result*10 + x%10
        x = x // 10
    return result

n, k = map(int,input().split())

n_list = [n*i for i in range(1, k+1)]

max_num = -1
for i in n_list:
    max_num = max(max_num, num_reverse(i))
print(max_num)