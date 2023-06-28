n = int(input())
n_list = [x for x in range(1, n + 1)]
while len(n_list) > 1:
    n_list.pop(0)
    n_list.append(n_list.pop(0))
print(n_list[-1])
