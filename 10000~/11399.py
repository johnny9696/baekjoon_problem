n  =  int(input())
n_list = list(map(int, input().split()))
n_list.sort()
result =[]
for i in range(n):
    if i == 0:
        result.append(n_list[i])
    else:
        result.append(result[i-1]+n_list[i])
print(sum(result))